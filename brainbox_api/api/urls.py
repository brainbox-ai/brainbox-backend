from django.urls import path
from .views import MessageListAV

urlpatterns = [
    path('prompts/', MessageListAV.as_view(), name="messagelist"),
]
