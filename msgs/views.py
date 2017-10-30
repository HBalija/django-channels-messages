# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import UserForm, MessageForm, UserLoginForm
from .models import Message


def frontpage(request):
    form = MessageForm()
    messages = Message.objects.all()

    context = {
        'messages': messages,
        'form': form
    }

    return render(request, 'index.html', context)


def user_login(request):
    if request.user.is_authenticated():
        return redirect('frontpage')

    form = UserLoginForm()

    if request.method == "POST":
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('frontpage')
            else:
                error = "Wrong username or password."
                return render(request, 'login.html', {'form': form, 'login_error': error})

    return render(request, 'login.html', {'form': form})


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


@csrf_exempt
def ajax_sort_messages(request):

    mess_id = request.GET.get('mess_id')

    messages = Message.get_messages(mess_id=mess_id)
    parsed_messages = [mess.message_data for mess in messages]

    return JsonResponse({'mess': parsed_messages}, status=200)
