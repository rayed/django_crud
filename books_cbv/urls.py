from django.urls import path

from . import views

app_name = 'books_cbv'

urlpatterns = [
  path('', views.BookList.as_view(), name='book_list'),
  path('new', views.BookCreate.as_view(), name='book_new'),
  path('edit/<int:pk>', views.BookUpdate.as_view(), name='book_edit'),
  path('delete/<int:pk>', views.BookDelete.as_view(), name='book_delete'),
]