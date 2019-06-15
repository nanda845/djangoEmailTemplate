from django.conf.urls import url
from emailApp.views import *

urlpatterns=[
    url(r'^sending_mail/$', sendingMail)
]