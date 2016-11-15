#!/usr/bin/env python
#coding: utf-8

from django import forms

from company.models import Announcement

class FaqCategoryForm(forms.ModelForm):
    
    class Meta:
        model = Announcement
        exclude = ('content',)
