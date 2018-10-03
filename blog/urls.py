from django.conf.urls import url
from . import views
from . import views_cbv

app_name = "blog"

urlpatterns = [
    # FBV 기반 URL
    # url(r'^$', views.post_list, name='post_list'),
    # url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),


    # CBV 기반 URL
    url(r'^$', views_cbv.post_list, name='post_list'),
    url(r'^(?P<pk>\d+)/$', views_cbv.post_detail, name='post_detail'),
    url(r'^cbv/new/$', views_cbv.post_new, name='post_new'),
    url(r'^cbv/(?P<pk>\d+)/edit/$', views_cbv.post_edit, name='post_edit'),
    url(r'^cbv/(?P<pk>\d+)/delete/$', views_cbv.post_delete, name='post_delete'),


    # path('<int:id>/', views.post_detail, name='post_detail'),
]

