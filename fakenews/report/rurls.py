from django.conf.urls import url
from report import views

urlpatterns = [
    url('^rep/', views.rep),
    url('^repp/', views.repp),
    url(r'^approve/(?P<idd>\w+)',views.detect,name='approve'),
    url('reject/(?P<idd>\w+)',views.reject,name='reject')
]