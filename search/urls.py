from django.conf.urls import url, include
from . import views

urlpatterns = [
    #/search
    url(r'^$', views.index, name='index'),

    #/search/document/:id
    url(r'^(?P<document_id>[0-9]+)/$', views.documentDetail, name='documentDetail'),
]
