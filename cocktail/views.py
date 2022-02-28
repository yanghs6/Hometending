from django.shortcuts import render


def list(request):
    context = dict()

    return render(request, "list.html", context)

def recipes(request):
    context = dict()

    return render(request, "recipes.html", context)

# Create your views here.
