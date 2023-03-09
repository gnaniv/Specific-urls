from app1.views import *

from django.urls import path

app_name='some'

urlpatterns=[
    path('PSPK/',PSPK,name='PSPK')
]