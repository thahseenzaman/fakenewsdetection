from django.conf.urls import url
from pr import views

urlpatterns = [
    url('^up/', views.app),
    url('^bl/', views.block),
    url('^pr/', views.pro),
    url('^rej/', views.rej),



]