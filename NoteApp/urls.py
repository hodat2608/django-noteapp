from django.urls import path
from . import views 
from djoser import views as djoser_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.getRouter),
    path('All_Note/', views.NoteList.as_view()),
    path('Action/<str:pk>/', views.Action_note.as_view()),
]