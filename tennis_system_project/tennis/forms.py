from django import forms
from django.contrib.auth.models import User
from tennis.models import Player, Camp, Day, Session, Attendance, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
   class Meta:
       model = UserProfile
       fields = ('emergcon1', 'emergcon2')
