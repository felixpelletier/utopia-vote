from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = [
    url(r'^resultats', views.resultats, name='resultats'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^', views.index, name='index'),
]
