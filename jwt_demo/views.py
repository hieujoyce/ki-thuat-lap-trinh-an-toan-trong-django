
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize

class JwtDemoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        print(request.user.first_name)
        data = {
            "list": [1, 2, 3, 4, 5, 6],
            "userId": request.user.id,
            "isAdmin": request.user.is_staff
        }
        return Response(data)
