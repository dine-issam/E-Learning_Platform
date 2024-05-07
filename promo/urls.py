from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('promo/',views.PromoView.as_view()),
    path('promo/<int:pk>/',views.SinglePromoView.as_view()),
    path('chapitre/',views.ChapitreView.as_view()),
    path('chapitre/<int:pk>/',views.SingleChapitreView.as_view()),
    path('mooc/',views.MoocView.as_view()),
    path('mooc/<int:pk>/',views.SingleMoocView.as_view()),
    path('cours/',views.CoursView.as_view()),
    path('cours/<int:pk>/',views.SingleCoursView.as_view()),
    path('fiche/',views.FicheView.as_view()),
    path('fiche/<int:pk>/',views.SingleFicheView.as_view()),
    path('devoir/',views.DevoirView.as_view()),
    path('devoir/<int:pk>/',views.SingleDevoirView.as_view()),
    path('commentaire/',views.CommentaireView.as_view()),
    path('commentaire/<int:pk>/',views.SingleCommentaireView.as_view()),
    path('ressource/',views.RessourceView.as_view()),
    path('ressource/<int:pk>/',views.SingleRessourceView.as_view()),
    path('niveau/',views.NiveauView.as_view()),
    path('niveau/<int:pk>/',views.SingleNiveauView.as_view()),
    path('module/',views.ModuleView.as_view()),
    path('module/<int:pk>/',views.SingleModuleView.as_view()),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)