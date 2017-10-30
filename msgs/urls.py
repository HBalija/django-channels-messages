from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.frontpage, name="frontpage"),
    url(r'^login$', views.user_login, name="login"),
    url(r'^register$', views.user_register, name="register"),
    url(r'^logout$', views.user_logout, name="logout"),
    url(r'^json/messages/$', views.ajax_sort_messages, name="ajax_sort_messages"),
]
