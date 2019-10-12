from django.urls import path
from car_sale import views

urlpatterns = [
	path("", views.car_sale_home, name="car_sale_home"),
	path("add-new-car/", views.add_new_car, name="add_car"),
	path("<int:pk>/", views.car_detail, name="car_detail"),
]