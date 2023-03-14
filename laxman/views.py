from django.shortcuts import render

# Create your views here.
def ram(request):
    d={'name':'ramaiah'}
    return render(request,'ram.html',d)