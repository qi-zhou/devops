# Register your models here.
from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('UTF8')

import xadmin
from django.contrib.auth.models import Group, Permission
from sso_server.models import  *
from django.contrib.auth import get_user_model

User = get_user_model()


class GlobalSetting(object):
    menu_style = 'default'  # 'accordion'
    site_title = '后台管理'
    site_footer = 'IT支持中心'

    def get_site_menu(self):
        menu = (
            {'title': '权限管理', 'menus': (
                {'title': '组', 'icon': 'fa fa-users', 'perm': self.get_model_perm(Group, 'view'),
                 'url': self.get_model_url(Group, 'changelist')},
                {'title': '用户', 'icon': 'fa fa-user', 'perm': self.get_model_perm(User, 'view'),
                 'url': self.get_model_url(User, 'changelist')},
                {'title': '权限', 'icon': 'fa fa-lock', 'perm': self.get_model_perm(Permission, 'view'),
                 'url': self.get_model_url(Permission, 'changelist')},
            )},
        )
        return menu


class ConsumerAdmin(object):
    readonly_fields = ['public_key', 'private_key']
    list_display = ['name']


class Navadmin(object):
    list_display = ['name', 'url', 'style', 'ico', 'sort','fenlei']

class Noceadmin(object):
    list_display = ['desc','date']

class classadmin(object):
    list_display = ['name','sort']

xadmin.site.register(NavPage, Navadmin)
xadmin.site.register(notice, Noceadmin)
xadmin.site.register(classify, classadmin)

