from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def home(request):
    html = """
    <h1>Django - CRUD</h1>
    <a href="/books_cbv/">Datenbank</a><br>
    """
    return HttpResponse(html)