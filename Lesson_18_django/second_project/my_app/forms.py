from django import forms
from django.core.exceptions import ValidationError

class MyForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField()

    # validation of a specific field:
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) <= 3:
            raise ValidationError('Name is too short')
        return name

    # validation of all fields:
    def clean(self):
        print('Cleaning self')
        if self.cleaned_data.get('name', None) == 'Nikita':
            raise ValidationError('B0000!')

        return self.cleaned_data
