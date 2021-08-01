from django.conf.urls import url
from video import views
urlpatterns = [
    url('^vidu/',views.vide),
    url('^vidv/', views.viewvid),
    url('^vido/', views.viewv),

]