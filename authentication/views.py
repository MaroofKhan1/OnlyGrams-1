from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.

class SignUpView(View):
    template_name = 'authentication/signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        pass