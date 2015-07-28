from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def home(request):
    html = """
    <h1>Django CRUD Example</h1>
    <a href="/books_cbv/">Class Based Views</a><br>
    <a href="/books_fbv/">Function Based Views</a><br>    
    <a href="/books_fbv_user/">Function Based Views with User Access</a><br>    
    """
    return HttpResponse(html)