from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'psec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('psec.an_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
