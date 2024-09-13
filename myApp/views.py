from django.shortcuts import render
from django.contrib.auth.models import User



def home(request):
    name = 'Bektursun'
    surname = 'Asankojoev'

    context = {
        'name':name ,
        'surname':surname
    }

    return render(request, "home.html", context)



def admins(request):
    admin = User.objects.all()
    context = {
        'admins':admin,
    }
    return render(request,'admins.html', context)


