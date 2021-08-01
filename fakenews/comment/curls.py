from django.conf.urls import url
from comment import views

urlpatterns = [
    url('^pcom/',views.postcomment),
    url('^vwcom/',views.viewcomment),

]