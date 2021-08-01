from django.conf.urls import url
from removal_request import views
urlpatterns=[
    url('rem/',views.removal),
    url('viewre/',views.viewrew),
    url('unblock/(?P<idd>\w+) (?P<uid>\w+)',views.unblock,name='unblock')
    # url('reg/',views.reg)

]