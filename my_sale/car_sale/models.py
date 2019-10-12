from django.db import models

class Make (models.Model):
	car_mak = models.CharField(max_length=255, default = 'not_null')

	def __str__(self):
		return self.car_mak

	class Meta:
		verbose_name = "Make"
		verbose_name_plural = "Make list"

class Model(models.Model):
	car_make_mod = models.ForeignKey(
			Make, 
			verbose_name='Car make (model)', 
			related_name='carMakeMod',
			default='not_null',  
			on_delete=models.CASCADE
			)

	car_mod = models.CharField(max_length=255, default = 'not_null')

	def __str__(self):
		return self.car_mod
	
	class Meta:
		verbose_name = "Model"
		verbose_name_plural = "Model list"

class Year(models.Model):
	car_y = models.IntegerField(default = 1900)

	def __str__(self):
		return str(self.car_y)
	
	class Meta:
		verbose_name = "Year"
		verbose_name_plural = "Year list"

class Fuel(models.Model):
	car_f = models.CharField(max_length=255, default = '')

	def __str__(self):
		return str(self.car_f)
	
	class Meta:
		verbose_name = "Fuel"
		verbose_name_plural = "Fuel categories"

class Gearbox(models.Model):
	car_gearb = models.CharField(max_length=31, default = 'not_null')

	def __str__(self):
		return str(self.car_gearb)

	class Meta:
		verbose_name = "Gearbox"
		verbose_name_plural = "Gearbox variety"

class Layout(models.Model):
	car_lay = models.CharField(max_length=31, default = 'not_null')

	def __str__(self):
		return self.car_lay

	class Meta:
		verbose_name = "Layout"
		verbose_name_plural = "Layout variety"

class Car (models.Model):

	car_make = models.ForeignKey(
		Make, 
		verbose_name='Car make', 
		related_name='carMake',
		default='not_null',  
		on_delete=models.CASCADE
		)

	car_model = models.ForeignKey(
		Model, 
		verbose_name='Car model', 
		related_name='carModel',
		default='not_null', 
		on_delete=models.CASCADE
		)

	car_year = models.ForeignKey(
		Year, 
		verbose_name='Production year', 
		related_name='carYear',
		default=1900, 
		on_delete=models.CASCADE
		)

	car_fuel = models.ForeignKey(
		Fuel, 
		verbose_name='Fuel type', 
		related_name='carFuel',
		default='not_null', 
		on_delete=models.CASCADE
		)

	car_engine_volume = models.IntegerField( 
		verbose_name='Engine volume in cm3', 
		default=0, 
		)

	car_power = models.IntegerField(
		verbose_name = "Power",
		default = 0
		)

	car_gearbox = models.ForeignKey(
		Gearbox, 
		verbose_name='Gearbox', 
		related_name='carGearbox',
		default='gearbox', 
		on_delete=models.CASCADE
		)

	car_layout = models.ForeignKey(
		Gearbox, 
		verbose_name='Layout', 
		related_name='carLayout',
		default='layout', 
		on_delete=models.CASCADE
	)

	#car_price = models.IntegerField(verbose_name = "Price in USD", default = 0)

	'''def __str__(self):
		return str(("Make: {}\nModel: {}\nYear: {}\nFuel: {}\nEngine volume: {}\nPrice in USD: {}".format(
			car_make,
			car_model, 
			car_year,
			car_fuel,
			car_engine_volume,
			car_price)))'''

	class Meta:
		verbose_name = "Car"
		verbose_name_plural = "Car list"
	# Create your models here.
