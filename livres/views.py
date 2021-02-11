# Create your views here.
from .models import Auteur, Livre

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AuteurSerializer, LivreSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class AuteursApi(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = AuteurSerializer
    queryset = Auteur.objects.all()
    lookup_field = "id"

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        if "livres" in request.data:
            request.data.pop("livres")
        auteur = Auteur.objects.create(**request.data)
        serializer = AuteurSerializer(auteur)
        return Response(serializer.data)

    def put(self, request, id):
        if "livres" in request.data:
            request.data.pop("livres")
        auteur = Auteur.objects.filter(id=id).update(**request.data)
        serializer = AuteurSerializer(auteur)
        return Response(serializer.data)

    def delete(self, request, id):
        return self.destroy(request)


class LivresApi(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = LivreSerializer
    queryset = Livre.objects.all()
    lookup_field = "id"

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id):
        return self.update(request)

    def delete(self, request, id):
        return self.destroy(request)