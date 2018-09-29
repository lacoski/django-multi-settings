from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.models import User
from .models import User

# Create your views here.

def index(request, session_openstack='None'):
    """
    Portal index
    """
    print(request.user.id)
    user = User.objects.get(pk=request.user.id)
    print(user.is_sale)
    print(user.is_technician)
    return HttpResponse('Check')