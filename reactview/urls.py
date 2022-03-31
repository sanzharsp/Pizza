
from django.urls import path
from .views import *


urlpatterns = [
   path('',index,name='index'),
   path('pizzas/',load.as_view()),
   path('manifest.json',Manifest.as_view()),

 
   
]
