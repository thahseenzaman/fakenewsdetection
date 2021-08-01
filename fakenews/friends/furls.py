from django.conf.urls import url
from friends import views

urlpatterns = [
    url('^frnd/', views.frnd_key),
    url('^srnd/', views.send_reg),
    url('^vrnd/',views.view_reg),
    url('^fapprove/(?P<idd>\w+)',views.fapprove,name='fapprove'),
    url('^freject/(?P<idd>\w+)',views.freject,name='freject')

]
