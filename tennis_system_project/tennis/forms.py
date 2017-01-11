from django import forms
from django.contrib.auth.models import User
from tennis.models import Player, Camp, Day, Session, Attendance, UserProfile
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, Form

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
   class Meta:
       model = UserProfile
       fields = ('emergcon1', 'emergcon2')

class PlayerForm(forms.ModelForm):
   fname = forms.CharField(max_length=30, label='First Name')
   sname = forms.CharField(max_length=30, label='Surname')
   medicalcons = forms.CharField(max_length=128, label='Medical Conditions')
   btmno = forms.IntegerField(label='BTM Number', required=False)
   dob = forms.DateField(widget=SelectDateWidget(years=range(1917,datetime.datetime.now().year), label='Date of Birth')

   class Meta:
      model = Player
      # exclude foreign key field
      exclude = ('person',)
