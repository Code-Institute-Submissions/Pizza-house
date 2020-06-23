from django.shortcuts import render, redirect
from .models import Recipe
# Create your views here.

pizza = Recipe.objects.filter(category='PIZZA')
hamburger = Recipe.objects.filter(category='HAMBURGER')
pasta = Recipe.objects.filter(category='PASTA')
salad = Recipe.objects.filter(category='SALAD')
kebab = Recipe.objects.filter(category='KEBAB')

def home(request):
    return render(request, 'orders/home.html')

def menu(request):
    context = {
        'pizza': pizza,
        'kebab': kebab,
        'pasta': pasta,
        'salad': salad,
        'hamburger': hamburger,
    }
    return render(request, 'orders/menu.html', context)

def pizza_menu(request):
    context = {
        'pizza': pizza,
    }
    return render(request, 'orders/pizza.html', context)


def kebab_menu(request):
    context = {
        'kebab': kebab,
    }
    return render(request, 'orders/kebab.html', context)

def salad_menu(request):
    context = {
        'salad': salad,
    }
    return render(request, 'orders/salad.html', context)

def pasta_menu(request):
    context = {
        'pasta': pasta,
    }
    return render(request, 'orders/pasta.html', context)

def hamburger_menu(request):
    context = {
        'hamburger': hamburger,
    }
    return render(request, 'orders/hamburger.html', context)