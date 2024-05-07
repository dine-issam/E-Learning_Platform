from rest_framework import serializers
from .models import Mooc, Promo,Chapitre,Fiche,Cours,Devoir,Commentaire,Ressource,Niveau,Module

class PromoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = '__all__'

class ChapitreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapitre
        fields = '__all__'
class MoocModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mooc
        fields = '__all__'
class CoursModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = '__all__'
class FicheModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fiche
        fields = '__all__'
class DevoirModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devoir
        fields = '__all__'
class CommentaireModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'
class RessourceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ressource
        fields = '__all__'
class NiveauModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveau
        fields = '__all__'
class ModuleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'