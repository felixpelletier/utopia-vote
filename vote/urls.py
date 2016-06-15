from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = [
    url(r'^resultats', views.resultats, name='resultats'),
    url(r'^', views.index, name='index'),
]
