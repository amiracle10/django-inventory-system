from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Discussion
from .models import Comment

class CustomUserCreationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username is already taken.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        if password.isnumeric():
            raise ValidationError("Password can't be entirely numeric.")
        if password.islower() or password.isupper():
            raise ValidationError("Password must contain both uppercase and lowercase letters.")
        return password
    
class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['title','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] 