#!/usr/bin/env python
#coding: utf-8
from django.conf.urls import url
#from django.contrib.auth import views as auth_views
from blog import views



urlpatterns = [
    url(r'^$', views.index),  
    url(r'^archive/$', views.archive, name='archive'),#文章归档
    url(r'^article/$', views.article, name='article'),#文章
    url(r'^add_article/$', views.add_article, name='add_article'),#发表文章
    url(r'^comment/post/$', views.comment_post, name='comment_post'),#提交评论
    url(r'^logout$', views.do_logout, name='logout'),#登出
    url(r'^reg', views.do_reg, name='reg'),#注册
    url(r'^login', views.do_login, name='login'),#登陆
    url(r'^category/$', views.category, name='category'),#分类    
]
urlpatterns +=[
    url(r'^accounts/changepwd/$', views.changepwd,name='changepwd'),#修改密码
    url(r'^forgot-password/$',views.forgot_password, name="forgot_password"),#自定义邮件修改密码，过程发邮件等
    url(r'^resetpassword/passwordsent/$',views.password_reset_done,name='password_reset_done'),#修改密码完成跳转,名称不可修改
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',views.password_reset_confirm,name='password_reset_confirm'),
    url(r'^reset/done/$',views.password_reset_complete,name='password_reset_complete'),
] 