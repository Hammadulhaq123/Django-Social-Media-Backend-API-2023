from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html', context={"title": "Hello"})


def api(request):
    return render(request, 'list.html', context={"title": "List"})
