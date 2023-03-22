from django.shortcuts import render
#from django.core.cache import cache
#from .untils import cache
# Create your views here. session_view

# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip

def session_view(request):
    print(request.COOKIES.get('sessionid'))
    request.session['fav_color'] = 'red'
    ctx = {
        "fav_color": ""
    }
    ctx['fav_color'] = request.session.get('fav_color', 'black')
    return render(request, 'session.html', ctx)
