
from django.urls import path
from .views import home, admins

urlpatterns = [

    path('in/', home, name='home'),
    path('admins/', admins, name='admins')
]
