from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponse
from .models import Card, Tag

# Create your views here.


def loginPage(request):
    return


def logoutPage(request):
    return


def registerPage(request):
    return


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    cards = Card.objects.all().order_by('-created')
    card_count = cards.count()

    context = {'cards': cards, 'card_count': card_count}

    return render(request, 'base/home.html', context)
