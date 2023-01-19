from django.shortcuts import render
from .models import QrCode
def med(request):
    return render(request,'qr/home.html')

def create_qr(request):
    if request.method=="POST":
        subject = request.POST['subject']
        QrCode.objects.create(url='https://www.tutorialspoint.com/qr-code-generating-website-in-django')
    qr_code=QrCode.objects.all()
    return render(request,'qr/create_qr.html',{"qr":qr_code})

def student(request):
    return render(request, 'qr/student.html')
