"""fakenews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf.urls import url,include
from login import views

urlpatterns = [

     url(r'^$',views.log),
     url(r'^comp/',include('complaint.curls')),
     url(r'^comment/',include('comment.curls')),
     url(r'^feedback/',include('feedback.furls')),
     url(r'^friends/',include('friends.furls')),
     url(r'^image/',include('image.iurls')),
     url(r'^login/',include('login.lurls')),
     url(r'^news/',include('news.nurls')),
     url(r'^report/',include('report.rurls')),
     url(r'^user/',include('user.uurls')),

     url(r'^video/',include('video.vurls')),
     url(r'^pr/',include('pr.purls')),
     # url(r'^prof/',include('request.ruls')),
     url(r'^rem/',include('removal_request.url')),




]
