
from django.contrib import admin
from django.urls import path
from Executor.views import home , login , run_code  ,problems  ,get_data
urlpatterns = [
    path('', home , name= 'home') , 
    path('problems/<int:pk>', problems , name= 'problems') , 
    path('login/', login , name= 'login') , 
    path('run_code/', run_code , name= 'runcode') , 
    path('get_data/<int:pk>' , get_data , name = 'api1'), 
]
