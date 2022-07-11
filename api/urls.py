from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path("notes/", views.getNotes),
    path("notes/create", views.createNotes),
    path("notes/<int:pk>/update", views.updateNotes),
    path("notes/<int:pk>/delete", views.deleteNotes),
    path("notes/<int:pk>", views.getNote),
]
