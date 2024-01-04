from django.shortcuts import render
from .models import *

# Create your views here.
def home(req):
    return render(req,'home.html')

def product(req):
    product = Items.objects.all()
    return render(req,'product.html',{'product':product})