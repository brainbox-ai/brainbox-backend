from django.urls import path
from brainbox.api.views import MessageListAV

urlpatterns = [
    path('prompts/', MessageListAV.as_view(), name="messagelist"),
]
