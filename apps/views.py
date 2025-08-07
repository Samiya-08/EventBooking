from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Event, User
from .serializers import EventSerializer, UserCreateSerializer


class EventCreateView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

class EventRegisterView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            event.participants.add(request.user)
            return Response({'success': 'Eventga ro‘yxatdan o‘tildi'}, status=status.HTTP_200_OK)
        except Event.DoesNotExist:
            return Response({'error': 'Bunday event yo‘q'}, status=status.HTTP_404_NOT_FOUND)


class MyRegisteredEventsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(participants=self.request.user)