from django.conf.urls import url
from news import views

urlpatterns = [
    url('^fakec/',views.fakec),
    url('^news/',views.news),
    # url('^up/', views.up),
    url('^updatet/', views.update),
    url('^viewn/', views.viewn),

    url('updatenew/(?P<idd>\w+)',views.updatenew,name='updatenew'),
    url('reason/(?P<idd>\w+)',views.reason,name='reason'),
    url('newspub/',views.newspublic),
    url('viewfake/',views.viewfake),

]