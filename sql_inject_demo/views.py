from django.shortcuts import render
from .models import Userct
from django.http import HttpResponse
#from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_deny

#@xframe_options_deny
def sqlViewNotSecurity(request):
    if request.method == "POST":
        name = request.POST.dict().get("username")
        pw = request.POST.dict().get("password")
        sql = "SELECT * FROM sql_inject_demo_userct WHERE username = '{0}' AND password = '{1}'".format(name, pw)
        user = Userct.objects.raw(sql)
        if(len(user) > 0):
            return HttpResponse("Dang nhap thanh cong")
        else:
            return HttpResponse("Tai khoan hoac mat khau khong chinh xac")
    else: 
        return render(request, 'sql_not_security.html')
    
def sqlViewSecurity(request):
    if request.method == "POST":
        name = request.POST.dict().get("username")
        pw = request.POST.dict().get("password")
        user = Userct.objects.filter(username=name, password=pw)
        if(len(user) > 0):
            return HttpResponse("Dang nhap thanh cong")
        else:
            return HttpResponse("Tai khoan hoac mat khau khong chinh xac")
    else: 
        return render(request, 'sql_security.html')
