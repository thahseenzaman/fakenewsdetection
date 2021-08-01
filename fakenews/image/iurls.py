from django.conf.urls import url
from image import views

urlpatterns = [
    url('^uimg/', views.uploadimage),
    url('^vimg/', views.viewimage),
    url('^imagepubl/', views.imagepub),

]
