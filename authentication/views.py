# from django.http import HttpRequest, HttpResponse
from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from authentication.forms import UserForm
from django.contrib.auth import authenticate, login
# Create your views here.

def home(request):
    return HttpResponse('home')
    

class SignInView(View):
    template_name = 'authentication/signin.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is None:
            return render(request, self.template_name)
        login(request, user)
        return redirect('home_feed')
        # this is where we are going to define user login above our sign up



class SignUpView(View):
    template_name = 'authentication/signup.html'
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_view')
        
        context = {'form': form}


        return render(request, self.template_name)
        