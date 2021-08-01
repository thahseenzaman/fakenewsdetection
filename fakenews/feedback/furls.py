from django.conf.urls import url
from feedback import views

urlpatterns = [
    url('^pfeed/', views.postfeed),
    url('^vfeed/', views.viewfeed),

]
