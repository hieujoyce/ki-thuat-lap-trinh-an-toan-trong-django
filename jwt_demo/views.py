
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize
import json
# from django.contrib.auth.models import User

# lname = 'hieujoyce'
# user = User.objects.raw('SELECT * FROM users WHERE username = %s', [lname])
# print(user)

# Create your views here.
#json.dumps(myobject.__dict__) request.user

class JwtDemoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        
        # for item in request.user:
        #     print(item)
        # serialized_data = serialize("json", request.user)
        # serialized_data = json.loads(serialized_data)
        print(request.user.first_name)
        data = {
            "list": [1, 2, 3, 4, 5, 6],
            "userId": request.user.id,
            "isAdmin": request.user.is_staff
        }
        return Response(data)
