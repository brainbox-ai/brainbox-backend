from django.urls import path
from . import views

urlpatterns = [
    path('prompts/', views.MessageListAV.as_view(), name="messagelist"),
    path('RandomCharacterResponse/', views.RandomMessageListAV.as_view(), name="RandomCharacterResponse"),
]
