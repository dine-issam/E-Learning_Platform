
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('promo/', include('promo.urls')), 
    path('api/v1/auth/',include('accounts.urls')),
    path('etudiant/', include('csv_app.urls')), 
    path('quiz/', include('quizes.urls', namespace='quizes'))


]
