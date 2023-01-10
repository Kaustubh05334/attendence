from django.shortcuts import render

def med(request):
    return render(request,'qr/home.html')

def create_qr(request):
    return render(request,'qr/create_qr.html')

def student(request):
    return render(request, 'qr/student.html')
