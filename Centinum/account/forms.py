from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User
from django_countries import Countries


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    CHOICES = [
        ('Innovator', 'Innovator'),
        ('Investor', 'Investor'),
        ('Entrepreneur', 'Entrepreneur')
    ]
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}), label_suffix="")
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-control'}), label_suffix="")
    usertype = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), label_suffix="",label='Register as', required=True)
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label_suffix="")
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             label_suffix="")

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            profile = Profile.objects.create(user=user)
        return user


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=12, min_length=12, widget=forms.TextInput(attrs={'placeholder': '00 3241 xxx xxxx'}))
    country = forms.ChoiceField(choices=Countries)

    class Meta:
        model = Profile
        fields = ('address', 'profile_image', 'profession', 'zip_code', 'phone_number', 'country', 'street', 'town')
