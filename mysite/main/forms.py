from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Vote
from django.forms.widgets import NumberInput

class NewUserForm(UserCreationForm):
	email=forms.EmailField(required=True)
	
	class Meta:
		model=User #based on user model
		fields=("username","email","password1","password2")


		
	#email field to our registration form
	def save(self,commit=True):
		user=super(NewUserForm,self).save(commit=True)
		user.email=self.cleaned_data['email']
		if commit:
			user.save()
		return user
	
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
	class Meta: 
		model = Profile
		fields = ('products',)

class VoteForm(forms.ModelForm):
	comfort=forms.IntegerField(widget=NumberInput(attrs={'placeholder': ('5'),'type':'range', 'min': '1', 'max': '10', 'class': 'comfort'}))
	performance = forms.IntegerField(widget=NumberInput(attrs={'placeholder': ('5'),'type':'range', 'min': '1', 'max': '10', 'class': 'performance'}))
	durability = forms.IntegerField(widget=NumberInput(attrs={'placeholder': ('5'),'type':'range', 'min': '1', 'max': '10', 'class': 'durability'}))

	class Meta: 
		model = Vote
		fields = ('comfort','performance','durability')