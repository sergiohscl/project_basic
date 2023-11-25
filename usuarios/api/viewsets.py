from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import views
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
from usuarios.api.serializer import CustomUserSerializer


User = get_user_model()


class CustomUserApiView(views.APIView):
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ["get", ]

    @swagger_auto_schema(
        responses={200: CustomUserSerializer(many=True)},
    )
    def get(self, request):
        usuarios = User.objects.all()
        serializer = CustomUserSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
