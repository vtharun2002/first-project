from email.mime import image
from django.shortcuts import render

# Create your views here.
def function1(request):
    return render(request,'first.html')

def function2(request):
    return render(request,'second.html')