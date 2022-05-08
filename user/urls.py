#!/user/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from django.views.static import serve
from health_monitoring import settings
from .views import *
from . import viewsUtil
from django.conf.urls import url,re_path

app_name = 'user'

urlpatterns = [
    url(r'^register/$', register, name="register"),
    url(r'^register_handle/$', register_handle, name="register_handle"),
    url(r'^register_exist/$', register_exist, name="register_exist"),
    url(r'^login/$', login, name="login"),
    url(r'^login_handle/$', login_handle, name="login_handle"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^findpwdView/$', findpwdView,name="findpwdView"),
    url(r'^verify_show/$', verify_show,name="verify_show"),
    url(r'^form/$', form, name="form"),
    url(r'^verifycode/$', viewsUtil.verify_code,name="verifycode"),
    url('^$', index, name="index"),
    re_path('^media/(?P<path>.*)/$',serve,{'document_root':settings.MEDIA_ROOT}),
]