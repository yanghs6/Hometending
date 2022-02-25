from django.shortcuts import render


def exam1(request):
    context = dict()
    
    return render(request, "exam1.html", context)

# Create your views here.
