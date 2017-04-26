# _*_ coding: utf-8 _*_
__author__ = 'Jack Zhou'

import xadmin
from .models import Host, HostGroup


class HostAdmin(object):
    list_display = ['hostname', 'ip', 'osversion', 'memory', 'disk', 'cpu_core']


class HostGroupAdmin(object):
    list_display = ['groupname']


xadmin.site.register(Host, HostAdmin)
xadmin.site.register(HostGroup, HostGroupAdmin)
