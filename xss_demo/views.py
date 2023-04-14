from django.shortcuts import render
import urllib

def security_view(request):
    
    ctx = {
        "className": ""
    }
    if request.method == "POST":
        className = request.POST.dict().get("className")
        ctx["className"] = urllib.parse.quote(className)
    return render(request, 'xss_security.html', ctx)

def not_security_view(request):
    
    ctx = {
        "className": ""
    }
    if request.method == "POST":
        className = request.POST.dict().get("className")
        ctx["className"] = className
    return render(request, 'xss_not_security.html', ctx)

