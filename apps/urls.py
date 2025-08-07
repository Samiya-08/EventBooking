from django.urls import path
from .views import (
    EventCreateView,
    RegisterView,
    EventRegisterView,
    MyRegisteredEventsView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('events/create/', EventCreateView.as_view(), name='event-create'),
    path('events/<int:pk>/register/', EventRegisterView.as_view(), name='event-register'),
    path('events/my-registered/', MyRegisteredEventsView.as_view(), name='my-registered-events'),
]


