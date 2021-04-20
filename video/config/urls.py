#!/usr/bin/env python
# -*- coding:utf8 -*-
# filename：urls.py
# Power by kevin.h 2021-04-21 00:20:49

from django.contrib import admin
from django.urls import path, include

from app.dashboard import urls as dashboard_url
from app.client import urls as cilent_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard', include(dashboard_url)),
    path('cilent', include(cilent_url))
    
]


