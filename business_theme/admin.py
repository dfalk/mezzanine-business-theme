#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.core.admin import SingletonAdmin
from mezzanine.pages.admin import PageAdmin

from business_theme.models import HomePage, Slide, IconBlurb, SitewideContent


class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class IconBlurbInline(TabularDynamicInlineAdmin):
    model = IconBlurb

class HomePageAdmin(PageAdmin):
    inlines = (SlideInline, IconBlurbInline)


admin.site.register(HomePage, HomePageAdmin)
admin.site.register(SitewideContent, SingletonAdmin)