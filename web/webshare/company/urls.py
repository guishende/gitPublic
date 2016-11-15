#!/usr/bin/env python
# coding: utf-8
from django.conf.urls import url
from company import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^faq$', views.faq),
    url(r'^faq/(?P<catid>\d{1,15})$', views.faq_cat_detail),
    url(r'^about$', views.about),
    url(r'^about/(?P<catid>\d{1,15})$', views.about_cat_detail),
    url(r'^service$', views.service),
    url(r'^service/(?P<catid>\d{1,15})$', views.service_cat_detail),
    url(r'^product$', views.products),
    url(r'^product/(?P<catid>\d{1,15})$', views.product_cat_detail),
    url(r'^download$', views.download),
    url(r'^download/(?P<catid>\d{1,15})$', views.download_cat_detail),
    url(r'^news/$', views.news),
    url(r'^news/(?P<newsid>\d{1,15})$', views.news_detail),
    
    
]
