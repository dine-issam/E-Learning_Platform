from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
cours_validator = FileExtensionValidator(['ppt', 'pdf','docx'])
mooc_validator = FileExtensionValidator(['mp4','mov','webm','avi','mkv','ogg','wmv'])
ressource_validator = FileExtensionValidator(['rar', 'zip'])


class Promo(models.Model):
    nom = models.CharField(max_length=20)
    spécialité = models.CharField(max_length=20)
    annee = models.CharField(max_length=10,default='2023-2024')
    def __str__(self):
        return self.nom
    
class Niveau (models.Model):
    nom = models.CharField(max_length=20)
    Promotion = models.ForeignKey(Promo, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom


    
class Module(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    Niveau = models.ForeignKey(Niveau,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom
    

   

class Chapitre(models.Model):
    
    date_deposer = models.DateTimeField(auto_now_add=True)
    nom = models.CharField(max_length=20)
    Module = models.ForeignKey(Module, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
    
class Mooc(models.Model):
    file = models.FileField(upload_to='uploads/',validators=[mooc_validator])
    nom = models.CharField(max_length=100, blank=True)
    duree =models.CharField(max_length=20)
    Chapitre=models.ForeignKey(Chapitre,   
        on_delete=models.CASCADE)
    
class Cours(models.Model):
    nom = models.CharField(max_length=50)
    file = models.FileField(upload_to='uploads/',validators=[cours_validator])
    Chapitre=models.ForeignKey(Chapitre,  
        on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
    
class Fiche(models.Model):
    nom = models.CharField(max_length=50)
    file = models.FileField(upload_to='uploads/',validators=[cours_validator])
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=50)
    Chapitre=models.ForeignKey(Chapitre, 
        
        on_delete=models.CASCADE)
class Devoir(models.Model):
    nom = models.CharField(max_length=50)
    date_debut = models.DateField(auto_created=True)
    date_fin = models.DateField(blank=True, null=True)
    file = models.FileField(upload_to='uploads/',validators=[cours_validator])
    Chapitre=models.ForeignKey(Chapitre, 
        on_delete=models.CASCADE)
class Commentaire(models.Model):
    contenu = models.CharField(max_length=500)
    temps = models.DateField(auto_created=True)
    Cours=models.ForeignKey(Cours, 
        on_delete=models.CASCADE)
class Ressource(models.Model):
    description = models.CharField(max_length=500)
    file = models.FileField(upload_to='uploads/',validators=[ressource_validator], blank=True, null=True)
    lien = models.CharField(max_length=200,blank=True,null=True)
    Chapitre=models.ForeignKey(Chapitre, 
        on_delete=models.CASCADE)

