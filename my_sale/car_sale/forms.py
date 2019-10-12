from django import forms
from car_sale.models import *

class new_car(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('car_make', 'car_model', 'car_year', 'car_fuel', 'car_engine_volume', 'car_power', 'car_gearbox', 'car_layout')