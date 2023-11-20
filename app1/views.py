from django.shortcuts import render

# Create your views here.
def conditions(request):
    d = {'a':10,'b':150,'c':200}
    return render(request,'condition.html',d)
def aplication(request):
    d = {'a':10,'b':150,'c':200}
    return render(request,'apps.html',d)