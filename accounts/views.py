from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User # Or your custom user model
from .forms import CustomUserCreationForm

# Create your views here.
class SignUpView(CreateView):
    # 1. Which form to use
    form_class = CustomUserCreationForm
    
    # 2. Where to redirect the user after a successful sign-up
    # reverse_lazy is used to look up the URL name once the project's URLconf is loaded
    success_url = reverse_lazy('login') # Redirects to Django's built-in login view
    
    # 3. Which model the form creates an object for
    model = User 
    
    # 4. Which template to render the form on
    template_name = 'registration/signup.html'