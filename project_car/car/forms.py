from django import forms
from .models import Car

class AddCarForm (forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

        labels = {
            'name' : 'Car Model / Name',
            'year' : 'Manufacturing Year',
        }

        widgets = {
            'name' : forms.TextInput(attrs={'type':"text", 'class':"form-control border-start-0 ps-0", 'id':"name", 'name':"name", 'placeholder':"e.g. Toyota Corolla"}),
            'year' : forms.NumberInput(attrs={'type':"number", 'class':"form-control border-start-0 ps-0", 'id':"year", 'name':"year", 'placeholder':"e.g. 2024"}),
        }

        error_messages = {
            'year' : {
                'min_value' : "min manufacturing  year is 2000"
            }
        }