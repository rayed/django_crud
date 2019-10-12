from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.db.models import F
from car_sale.models import *
from car_sale.forms import new_car
import logging

#source venv/bin/activate
logger = logging.getLogger(__name__)

def car_sale_home(request):

	cars = Car.objects.all()
	context = {
		'cars': cars
	}


	return render(request, 'car_sale_home.html', context)

#fields = ('car_make', 'car_model', 'car_year', 'car_fuel', 'car_engine_volume', 'car_price')

def add_new_car(request):
	if request.method == 'POST':
		form = new_car(request.POST)
		if form.is_valid():
			car_make = form.cleaned_data['car_make']


			#Room.objects.select_related('house').filter(house__street=xyz)
			
			#car_model_search = car_sale.Model.objects.get(car_make_mod=car_make)
			#car_model_search.update()
			car_model_search = car_sale.Model.objects.get(car_make_mod__iexact = car_make)
			car_model_search.update()
			print(car_model_search)
			print("fuck you")
			car_model = form.cleaned_data[car_model_search]
			car_year = form.cleaned_data['car_year']
			car_fuel = form.cleaned_data['car_fuel']
			car_engine_volume = form.cleaned_data['car_engine_volume']
			car_power = form.cleaned_data['car_power']
			car_gearbox = form.cleaned_data['car_gearbox']
			car_layout = form.cleaned_data['car_layout']

			car = Car(
				car_make = car_make,
				car_model = car_model,
				car_year = car_year,
				car_fuel = car_fuel,
				car_engine_volume = car_engine_volume,
				car_power = car_power,
				car_gearbox = car_gearbox,
				car_layout = car_layout
			)

			car.save()

		return render(request, 'thank_you.html')

	else:
		form = new_car()

	return render(request, 'add_car.html', {'form': form})

def car_detail(request, pk):
	car = Car.objects.get(pk=pk)
	context = {
		'car': car
	}
	return render(request, 'car_detail.html', context)


# Create your views here.
