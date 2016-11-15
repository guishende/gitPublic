#!/usr/bin/env python
#coding: utf-8
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from blog import views



urlpatterns = [
    url(r'^$', views.index),  
    url(r'^archive/$', views.archive, name='archive'),#文章归档
    url(r'^article/$', views.article, name='article'),
    url(r'^comment/post/$', views.comment_post, name='comment_post'),
    url(r'^logout$', views.do_logout, name='logout'),#登出
    url(r'^reg', views.do_reg, name='reg'),#注册
    url(r'^login', views.do_login, name='login'),#登陆
    url(r'^category/$', views.category, name='category'),#分类
    
]
urlpatterns +=[
    url(r'^accounts/changepwd/$', views.changepwd,name='changepwd'),
    url(r'^forgot-password/$',views.forgot_password, name="forgot_password"),
    #url(r'^login2', auth_views.login, name='login2'),#登陆      
    url(r'^password/change/$',auth_views.password_change,name='password_change'),#修改密码
    url(r'^password/change/done/$',auth_views.password_change_done,name='password_change_done'),#密码修改完成
    url(r'^resetpassword/$',auth_views.password_reset,name='password_reset'),
    url(r'^resetpassword/passwordsent/$',auth_views.password_reset_done,name='password_reset_done'),
    url(r'^reset/done/$',auth_views.password_reset_complete,name='password_reset_complete'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',auth_views.password_reset_confirm,name='password_reset_confirm'),
] 