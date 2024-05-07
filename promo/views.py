
from rest_framework import generics

from .models import Promo,Chapitre,Mooc,Cours,Fiche,Devoir,Commentaire,Ressource,Niveau,Module


from .serializers import PromoModelSerializer,ChapitreModelSerializer,MoocModelSerializer,CoursModelSerializer,FicheModelSerializer,DevoirModelSerializer,CommentaireModelSerializer,RessourceModelSerializer,NiveauModelSerializer,ModuleModelSerializer
#Promo:
class PromoView(generics.ListCreateAPIView):
    queryset = Promo.objects.all()
    serializer_class = PromoModelSerializer


class SinglePromoView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PromoModelSerializer
    def get_queryset(self):
        return Promo.objects.filter(pk = self.kwargs['pk'])

#chapitre:

class ChapitreView(generics.ListCreateAPIView):
    queryset = Chapitre.objects.all()
    serializer_class = ChapitreModelSerializer

class SingleChapitreView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChapitreModelSerializer
    def get_queryset(self):
        return Chapitre.objects.filter(pk = self.kwargs['pk'])

#Moocs:

class MoocView(generics.ListCreateAPIView):
    queryset = Mooc.objects.all()
    serializer_class = MoocModelSerializer

class SingleMoocView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MoocModelSerializer
    def get_queryset(self):
        return Mooc.objects.filter(pk = self.kwargs['pk'])

#Cours:

class CoursView(generics.ListCreateAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursModelSerializer

class SingleCoursView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CoursModelSerializer
    def get_queryset(self):
        return Cours.objects.filter(pk = self.kwargs['pk'])

#Fiche_td_tp:

class FicheView(generics.ListCreateAPIView):
    queryset = Fiche.objects.all()
    serializer_class = FicheModelSerializer

class SingleFicheView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FicheModelSerializer
    def get_queryset(self):
        return Fiche.objects.filter(pk = self.kwargs['pk'])

#Devoir:

class DevoirView(generics.ListCreateAPIView):
    queryset = Devoir.objects.all()
    serializer_class = DevoirModelSerializer

class SingleDevoirView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DevoirModelSerializer
    def get_queryset(self):
        return Devoir.objects.filter(pk = self.kwargs['pk'])

#Commentaire_sur_cours:

class CommentaireView(generics.ListCreateAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireModelSerializer

class SingleCommentaireView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentaireModelSerializer
    def get_queryset(self):
        return Commentaire.objects.filter(pk = self.kwargs['pk'])

#Ressource:

class RessourceView(generics.ListCreateAPIView):
    queryset = Ressource.objects.all()
    serializer_class = RessourceModelSerializer

class SingleRessourceView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RessourceModelSerializer
    def get_queryset(self):
        return Ressource.objects.filter(pk = self.kwargs['pk'])


#Niveau:

class NiveauView(generics.ListCreateAPIView):
    queryset = Niveau.objects.all()
    serializer_class = NiveauModelSerializer

class SingleNiveauView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NiveauModelSerializer
    def get_queryset(self):
        return Niveau.objects.filter(pk = self.kwargs['pk'])

#Module:

class ModuleView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleModelSerializer

class SingleModuleView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ModuleModelSerializer
    def get_queryset(self):
        return Module.objects.filter(pk = self.kwargs['pk'])