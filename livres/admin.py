from django.contrib import admin
from .models import Livre
from .models import Auteur


# Register your models here.
admin.site.register(Livre)
admin.site.register(Auteur)
