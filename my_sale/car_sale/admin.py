from django.contrib import admin
from car_sale.models import *
# Register your models here.

@admin.register(Make)
class AdminCarMake(admin.ModelAdmin):
	list_display = ('id', 'car_mak')
	list_filter = ('car_mak',)

@admin.register(Model)
class AdminCarModel(admin.ModelAdmin):
	list_display = ('id','car_make_mod', 'car_mod')
	list_filter = ('car_mod',)

@admin.register(Year)
class AdminCarYear(admin.ModelAdmin):
	list_display = ('id', 'car_y')
	list_filter = ('car_y',)

@admin.register(Fuel)
class AdminCarFuel(admin.ModelAdmin):
	list_display = ('id', 'car_f')
	list_filter = ('car_f',)

@admin.register(Gearbox)
class AdminCarEngineVolume(admin.ModelAdmin):
	list_display = ('id', 'car_gearb')
	list_filter = ('car_gearb',)

@admin.register(Layout)
class AdminCarEngineVolume(admin.ModelAdmin):
	list_display = ('id', 'car_lay')
	list_filter = ('car_lay',)

@admin.register(Car)
class AdminCar(admin.ModelAdmin):
	list_display = ('car_make', 'car_model', 'car_year', 'car_fuel', 'car_engine_volume', 'car_power', 'car_gearbox', 'car_layout')
	list_filter = ('car_make',)