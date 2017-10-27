# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import User, Message


class UserAdmin(admin.ModelAdmin):
    model = User
    fk_name = 'user'


class MessagerAdmin(admin.ModelAdmin):
    model = Message
    fk_name = 'message'


admin.site.register(User, UserAdmin)
admin.site.register(Message, MessagerAdmin)
