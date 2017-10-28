# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect

from .forms import UserForm, MessageForm
from .models import Message


def frontpage(request):
    form = MessageForm()
    messages = Message.objects.all()
    # if request.method == 'POST' and request.user.is_authenticated():
    #     form = MessageForm(request.POST)
    #     if form.is_valid():
    #         message = form.save(commit=False)
    #         message.user = request.user
    #         message.save()
    context = {
        'messages': messages,
        'form': form
    }

    return render(request, 'index.html', context)


def user_login(request):
    if request.user.is_authenticated():
        return render(request, 'frontpage.html')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            return HttpResponseBadRequest()

        user = authenticate(username=username,
                            password=password)

        if user:
            login(request, user)
            return redirect('frontpage')

        else:
            return render(request, 'login.html',
                          {'login_error': "Wrong username or password."})

    return render(request, 'login.html')


@login_required
def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect('frontpage')


def user_register(request):
    user_form = UserForm()
    if request.user.is_authenticated():
        return render(request, 'register.html', {'form': user_form})

    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password'])
            login(request, user)
            return redirect('frontpage')

    return render(request, 'register.html', {'form': user_form})
