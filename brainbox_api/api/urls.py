from django.urls import path
from .views import MessageListAV, ProfileListAV
from .debates import DebateListAV


urlpatterns = [
    path('prompts/', MessageListAV.as_view(), name="messagelist"),
    path('debates/', DebateListAV.as_view(), name="debatelist"),
    path('profiles/', ProfileListAV.as_view(), name="profilelist"),
]
