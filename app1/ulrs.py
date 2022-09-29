from  django.urls import path
from app1.views import *
app_name='first'
urlpatterns = [
    path('function1/',function1,name='function1'),
]