# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
CSSSTYLE = (
    ('tile bg-red', '红色'),
    ('tile bg-green', '绿色'),
    ('tile bg-blue', '蓝色'),
    ('tile bg-yellow', '橘黄'),
    ('tile bg-grey', '灰色')
)


class Classify(models.Model):
    name = models.CharField(verbose_name=u"名字", max_length=20, blank=True)
    sort = models.IntegerField(verbose_name='排序', blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['sort']


class Notice(models.Model):
    desc = models.CharField(verbose_name='描述', max_length=200, blank=True, default='今日无消息')
    date = models.DateTimeField(verbose_name='日期', auto_now_add=True)

    def __unicode__(self):
        return self.desc

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = verbose_name


class NavPage(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name=u"描述")
    url = models.URLField(blank=True, verbose_name='链接地址')
    style = models.CharField(max_length=100, blank=True, choices=CSSSTYLE, verbose_name='颜色')
    ico = models.CharField(max_length=100, blank=True, verbose_name='图标', default='fa fa-')
    sort = models.IntegerField(blank=True, verbose_name='排序')
    fenlei = models.ForeignKey(Classify, verbose_name='分类', blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '导航配置'
        verbose_name_plural = verbose_name
        ordering = ['sort']
