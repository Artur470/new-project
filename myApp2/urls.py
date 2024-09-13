
from django.urls import path
from .views import home2

urlpatterns = [

    path('in2/', home2, name='home2')

]
