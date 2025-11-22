# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User # Use the default User model

class CustomUserCreationForm(UserCreationForm):
    # Add fields you want that aren't in the default UserCreationForm
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta(UserCreationForm.Meta):
        # Explicitly define all fields you want on the form
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)