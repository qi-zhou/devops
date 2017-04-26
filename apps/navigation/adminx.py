# _*_ coding: utf-8 _*_
__author__ = 'Jack Zhou'

import xadmin


from .models import Classify, Notice, NavPage

class ClassifyAdmin(object):
    search_fields = ['name', 'sort']
    list_filter = ['name', 'sort']
    list_display = ['name', 'sort']

class NoticeAdmin(object):
    list_display = ['desc', 'date']

class NavPageAdmin(object):
    search_fields = ['name', 'url', 'style', 'ico', 'sort', 'fenlei']
    list_filter = ['name', 'url', 'style', 'ico', 'sort', 'fenlei']
    list_display = ['name', 'url', 'style', 'ico', 'sort', 'fenlei']


xadmin.site.register(Classify, ClassifyAdmin)
xadmin.site.register(Notice, NoticeAdmin)
xadmin.site.register(NavPage, NavPageAdmin)