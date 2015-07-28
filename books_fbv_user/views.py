from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from books_fbv_user.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'pages']

@login_required
def book_list(request, template_name='books_fbv_user/book_list.html'):
    if request.user.is_superuser:
        book = Book.objects.all()
    else:
        book = Book.objects.filter(user=request.user)
    data = {}
    data['object_list'] = book
    return render(request, template_name, data)

@login_required
def book_create(request, template_name='books_fbv_user/book_form.html'):
    form = BookForm(request.POST or None)
    if form.is_valid():
        book = form.save(commit=False)
        book.user = request.user
        book.save()
        return redirect('books_fbv_user:book_list')
    return render(request, template_name, {'form':form})

@login_required
def book_update(request, pk, template_name='books_fbv_user/book_form.html'):
    if request.user.is_superuser:
        book= get_object_or_404(Book, pk=pk)
    else:
        book= get_object_or_404(Book, pk=pk, user=request.user)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('books_fbv_user:book_list')
    return render(request, template_name, {'form':form})

@login_required
def book_delete(request, pk, template_name='books_fbv_user/book_confirm_delete.html'):
    if request.user.is_superuser:
        book= get_object_or_404(Book, pk=pk)
    else:
        book= get_object_or_404(Book, pk=pk, user=request.user)
    if request.method=='POST':
        book.delete()
        return redirect('books_fbv_user:book_list')
    return render(request, template_name, {'object':book})
