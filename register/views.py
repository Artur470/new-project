from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import UserForm, LoginForm
from django.contrib.auth import authenticate
class RegisterView(TemplateView):
    template_name = "register/register.html"

    def get(self, request, *args, **kwargs):
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Registration successful')
        return HttpResponse('Registration error: ' + str(form.errors))


class LoginView(TemplateView):
    template_name = "register/Login.html"

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                return redirect('index')
            else:
                return HttpResponse("Error")

        return HttpResponse('Success')


