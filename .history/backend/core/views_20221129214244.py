from django.shortcuts import render
from django.http import HttpResponse

def index(request= 'index.html'):
  return render(request, template, {})