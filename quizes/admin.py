from django.contrib import admin

# Register your models here.
from .models import Quiz, Topic


admin.site.register(Quiz)
admin.site.register(Topic)