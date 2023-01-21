"""attendence URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from qr.views import med,create_qr,student
from account.views import login_page,logout_page,registeruser,forgot_pass
urlpatterns = [
    path('admin/', admin.site.urls),

    #qr
    path('',med),
    path('teacher/',create_qr),
    path('student/',student),

    #account
    path('signup/',registeruser),
    path('login/',login_page),
    path('logout/',logout_page),
    path('forgot/',forgot_pass)
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
