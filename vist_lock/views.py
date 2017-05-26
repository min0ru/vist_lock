from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse


# Create your views here.

def index(request):
    return render(request, 'vist_lock/index.html')


def open(request):
    return redirect('index')

