from django.conf.urls import url
from user import views
urlpatterns = [
    url('^approv/',views.approv),
    url('^frndr/', views.frndr,name='request'),
    url('^mana/', views.mana),
    url('^regis/', views.regis),
    url('^register/', views.register),
    url('sendr/', views.sendr),
    url('blkusr/',views.blockuser),
    url('block/(?P<idd>\w+)',views.block,name='block'),
    url('search/',views.search),
    url('sndr/(?P<idd>\w+)',views.sndrequest,name='sndr'),


]