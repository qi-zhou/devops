# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Host(models.Model):
    hostname = models.CharField(verbose_name=u"主机名", max_length=50)
    ip = models.GenericIPAddressField(verbose_name=u"ip地址", max_length=50)
    osversion = models.CharField(verbose_name=u"系统版本", max_length=50)
    memory = models.CharField(verbose_name=u"内存", max_length=50)
    cpu_core = models.CharField(verbose_name=u"cpu核数", max_length=50)
    disk = models.CharField(verbose_name=u"磁盘", max_length=50)

    class Meta:
        verbose_name = u"主机列表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.hostname
        # vendor_id = models.CharField(max_length=50)
        # model_name = models.CharField(max_length=50)

        # product = models.CharField(max_length=50)
        # Manufacturer = models.CharField(max_length=50)
        # sn = models.CharField(max_length=50)


# 主机名,IP地址,内存(GB),CPU核数,操作系统,数据盘/data(GB),所属项目,主要应用
class HostGroup(models.Model):
    groupname = models.CharField(max_length=50, verbose_name=u"主机组名")
    members = models.ManyToManyField(Host, verbose_name=u"主机")

    class Meta:
        verbose_name = u"主机组"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.groupname
