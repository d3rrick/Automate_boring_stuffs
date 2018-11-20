from django import forms

MY_CHOICES = (
    ('migori', 'migori'),
    ('makueni', 'makueni'),
)

class UploadForm(forms.Form):
    number = forms.CharField(widget= forms.Textarea(attrs={'id':'number'}))
    # location = forms.ChoiceField(choices=MY_CHOICES,widget= forms.TextInput(attrs={'id':'location'}))
    location= forms.CharField(label='What is your location?', widget=forms.Select(choices=MY_CHOICES))

class VerifyFarmer(forms.Form):
    number = forms.IntegerField()