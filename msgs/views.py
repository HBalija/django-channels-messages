# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect

from .forms import UserForm
from .models import Message


def frontpage(request):
    return render(request, 'index.html')


def user_login(request):
    if request.user.is_authenticated():
        messages.warning(request, "You are already logged in.")
        return render(request, 'frontpage.html')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            return HttpResponseBadRequest()

        user = authenticate(username=username,
                            password=password)

        if user:
            if user.is_active:
                login(request, user)
                redirect_url = request.POST.get('next') or 'frontpage'
                return redirect(redirect_url)
            else:
                return render(request, 'login.html',
                              {'login_error': "Account disabled"})
        else:
            return render(request, 'login.html',
                          {'login_error': "Wrong username or password."})

    return render(request, 'login.html')


@login_required
def user_logout(request):
    if request.user.is_authenticated():
        redirect_page = request.POST.get('current_page', '/')
        logout(request)
        messages.success(request, 'Thanks. You\'ve logged out successfully.')
        return redirect(redirect_page)
    return redirect('frontpage')


def user_register(request):
    user_form = UserForm()
    if request.user.is_authenticated():
        messages.warning(request, 'You are already registered and logged in.')
        return render(request, 'register.html', {'form': user_form})

    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)

            user.save()
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password'])

            # send_user_register_mail.delay(user.username, user.email)
            login(request, user)
            return redirect('frontpage')

    return render(request, 'register.html', {'form': user_form})
