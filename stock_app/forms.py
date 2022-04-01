from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from stock_app.models import PictureModel
from .models import CATEGORY_PICTURES


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        # self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Type your username'
        self.fields['email'].widget.attrs['placeholder'] = 'Type your username'

        # self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Type your password'

        # self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Type your confirmation password'

        for field in ['password1', 'username']:
            self.fields[field].help_text = None


choices = CATEGORY_PICTURES


class AddPictureForm(forms.ModelForm):
    class Meta:
        model = PictureModel
        fields = '__all__'
        exclude = ('like', 'date_created',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-5',
                                            'placeholder': 'Type your title here'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-5',
                                                 'placeholder': 'Type your description here'}),

            # 'image': forms.ImageField(),
            'category': forms.Select(choices=choices, attrs={'class': 'dropdown my-5'}),
        }
