from rest_framework import serializers
from .models import Auteur, Livre


class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = "__all__"


class AuteurSerializer(serializers.ModelSerializer):
    livres = LivreSerializer(many=True)

    class Meta:
        model = Auteur
        fields = ["id", "nom", "dateNais", "nationalite", "livres"]
