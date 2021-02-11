from django.urls import path
from . import views

urlpatterns = [
    path("auteurs", views.AuteursApi.as_view()),
    path("auteurs/<int:id>", views.AuteursApi.as_view()),
    path("livres", views.LivresApi.as_view()),
    path("livres/<int:id>", views.LivresApi.as_view()),
]