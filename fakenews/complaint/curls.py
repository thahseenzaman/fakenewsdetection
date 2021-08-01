from django.conf.urls import url
from complaint import views

urlpatterns = [
    url('^vwcmplnt/',views.viewcomplaint),
    # url('^reply/',views.reply),
    url('^complaint/',views.complaint),
    url('reply/(?P<idd>\w+)',views.reply,name='reply')

]