from django.conf.urls import patterns, include, url
import xadmin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'devops.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(xadmin.site.urls)),
)
