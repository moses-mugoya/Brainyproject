from django import forms
from .models import StartupBusiness, Ideas, IdeaInvestments
from django.forms import DateInput
from django_countries import Countries


class BusinessForm(forms.ModelForm):
    CHOICE1 = [
        ('Idea stage', 'Idea stage'),
        ('Startup stage', 'Startup stage'),
        ('Growth stage', 'Growth stage'),
        ('Mature stage', 'Mature stage'),

    ]
    CHOICE2 = [
        ('B2B', 'B2B'),
        ('B2B2B', 'B2B2B'),
        ('B2B2C', 'B2B2C'),
        ('B2B2G', 'B2B2G'),
        ('B2C', 'B2C'),
        ('C2C', 'C2C'),
        ('Government(B2G)', 'Government(B2G)'),
        ('Non-profit', 'Non-Profit')
    ]
    country = forms.ChoiceField(label='Please select your country', widget=forms.Select, choices=Countries)
    founding_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'datepicker', 'placeholder': 'yyyy-mm-dd'}),
                                      label='Founding date')
    company_name = forms.CharField(widget=forms.TextInput, required=True)
    stage = forms.ChoiceField(choices=CHOICE1)
    sector = forms.ChoiceField(choices=CHOICE2)

    class Meta:
        model = StartupBusiness
        fields = ('name', 'company_name', 'customer_model', 'pitch', 'pitch_video_url', 'tag_line', 'sector', 'full_address', 'stage', 'country', 'personal')


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = ('name', 'description', 'personal')


