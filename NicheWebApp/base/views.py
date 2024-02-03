from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.


def loginPage(request):
    return


def logoutPage(request):
    return


def registerPage(request):
    return


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    return render(request, 'base/home.html', {})
