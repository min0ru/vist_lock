from django.shortcuts import render
from django.shurtcuts import redirect

# Create your views here.

def index(request):
    return render(request, 'vist_lock/index.html')

def open(request):
    return redirect('vist_lock.views.index')
