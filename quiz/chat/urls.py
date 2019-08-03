from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^audience/$', views.audience, name='audience'),
    url(r'^(?P<player_number>[1-8]+)/$', views.player, name='player'),
]
