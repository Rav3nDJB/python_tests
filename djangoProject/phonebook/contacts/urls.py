from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^(?P<contact_id>[0-9]+)/$', views.detail, name='detail'),
        url(r'^create/$', views.create, name='create'),
]