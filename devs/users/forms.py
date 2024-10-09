from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile, Skills, Message


class CustomUserCreationForm(UserCreationForm):
    """Form for login page"""

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'input input--text'})


class ProfileForm(ModelForm):
    """Form for edit profile page"""

    class Meta:
        model = Profile
        profile_fields = Profile._meta.fields
        fields = [field.name for field in profile_fields if field.name not in ['id', 'user']]


class SkillForm(ModelForm):
    """Form for add skill to profile"""

    class Meta:
        model = Skills
        fields = '__all__'
        exclude = ['owner']

    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'input input--text'})


class MessageForm(ModelForm):
    """Form to write and send a message"""
    
    class Meta:
        model = Message
        fields = ['subject', 'body']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'input input--text'})
