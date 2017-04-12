from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'aitest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^logger$', views.logger, name='logger'),
    url(r'^thrower$', views.thrower, name='thrower'),
    url(r'^errorer$', views.errorer, name='errorer'),
]
