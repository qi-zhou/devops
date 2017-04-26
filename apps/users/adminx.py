# _*_ coding: utf-8 _*_
__author__ = 'Jack Zhou'

import xadmin
from xadmin import views

from .models import UserProfile, EmailVerifyRecord


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '运维管理中心'
    site_footer = '阿里巴巴'
    menu_style = 'accordion'


class UserProfileAdmin(object):
    list_display = ['nick_name', 'username', 'is_superuser', 'gender', 'moblile', 'is_active', 'date_joined', 'email']


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
