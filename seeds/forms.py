from django import forms
from django.forms import ModelForm
from .models import Seeds


class SeedForm(ModelForm):
    class Meta:
        model = Seeds
        fields = ('seed_name', 'seed_variety', 'seed_type', 'seed_planting_zone', 'germination_period',
                  'days_to_harvest', 'plant_spacing', 'row_spacing', 'plant_depth', 'sun_requirements',
                  'water_requirements')
        labels = {
            'seed_name': 'Enter Seed Name',
            'seed_variety': 'Enter Seed Variety',
            'seed_type': 'Enter Seed Type',
            'seed_planting_zone': 'Enter Planting Zone',
            'germination_period': 'Enter Germination Period',
            'days_to_harvest': 'Enter Days To Harvest',
            'plant_spacing': 'Enter Plant Spacing',
            'row_spacing': 'Enter Row Spacing',
            'plant_depth': 'Enter Plant Depth',
            'sun_requirements': 'Enter Sun Requirements',
            'water_requirements': 'Enter Water Requirements'
        }
        widgets = {
            'seed_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'seed_variety': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'seed_type': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'seed_planting_zone': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'germination_period': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'days_to_harvest': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'plant_spacing': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'row_spacing': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'plant_depth': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'sun_requirements': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'water_requirements': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:300px'})
        }