from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import views
from drf_yasg.utils import swagger_auto_schema
from plataforma.api.serializers import LivrosSerializer
from plataforma.models import Livros
from rest_framework import viewsets
from rest_framework import mixins


class LivrosApiView(views.APIView):
    serializer_class = LivrosSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ["get", ]

    @swagger_auto_schema(
        responses={200: LivrosSerializer(many=True)},
    )
    def get(self, request):
        livros = Livros.objects.all()
        serializer = LivrosSerializer(livros, many=True)
        return Response(serializer.data)


class LivrosViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (IsAuthenticated,)
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer
