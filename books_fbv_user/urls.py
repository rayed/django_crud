from django.urls import path

from . import views

app_name = 'books_fbv_user'

urlpatterns = [
  path('', views.book_list, name='book_list'),
  path('new', views.book_create, name='book_new'),
  path('edit/<int:pk>', views.book_update, name='book_edit'),
  path('delete/<int:pk>', views.book_delete, name='book_delete'),
]