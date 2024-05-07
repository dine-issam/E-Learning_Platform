from django.urls import path
from .views import CSVUploadView, PersonListCreateView

urlpatterns = [
    path('upload-csv/', CSVUploadView.as_view(), name='upload-csv'),
    path('etudiant/', PersonListCreateView.as_view(), name='person-list-create'),
]
