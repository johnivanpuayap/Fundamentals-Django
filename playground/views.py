from django.shortcuts import render
from django.http import HttpResponse


def calculate():
    x = 1
    y = 2
    return x


# Create your views here.
# request -> response
# request handler

def say_hello(request):
    # return HttpResponse('Hello World')

    # Using a template
    # return render(request, 'hello.html', )

    x = calculate()
    # Passing a Dictionary
    return render(request, 'hello.html', {'name': 'John Ivan Puayap'})
