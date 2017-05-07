from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include (admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),

]
