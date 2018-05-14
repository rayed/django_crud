from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from books_cbv.models import Book

class BookList(ListView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('books_cbv:book_list')

class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('books_cbv:book_list')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books_cbv:book_list')