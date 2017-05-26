from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect
import socket


# Create your views here.

def index(request):
    return render(request, 'vist_lock/index.html')


def open(request):
    open_lock()
    return redirect('index')


def open_lock():
    addr = settings.LOCK_SERV_ADDR
    port = settings.LOCK_SERV_PORT
    code = settings.LOCK_SERV_CODE
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(code, (addr, port))
    udp_socket.close()
