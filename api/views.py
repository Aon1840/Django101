from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
def home(request):
    return render(request,'index.html')

