from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'superlists.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

                       url(r'^(\d+)/$', 'lists.views.view_list',
                           name='view_list'
                       ),
                       url(r'^new$', 'lists.views.new_list', name='new_list'),
                       
    #url(r'^admin/', include(admin.site.urls)),
                       
)
