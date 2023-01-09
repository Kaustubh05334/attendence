from django.shortcuts import render

def med(request):

    d1 = {234:"kabfgd"}
    return render(request,'home.html',d1)
