from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework import serializers

from django.contrib.auth.models import User
from django.db.models import Q

from .models import Reminder
from .serializers import ReminderSerializer

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class ReminderListCreateView(generics.ListCreateAPIView):
    serializer_class = ReminderSerializer

    # manual adding codes JWT Authentication and Permissions
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Reminder.objects.filter(user=self.request.user)

        status = self.request.query_params.get('status')
        date = self.request.query_params.get('date')
        message = self.request.query_params.get('message')
        priority = self.request.query_params.get('priority')

        if status:
            queryset = queryset.filter(status=status)

        if date:
            queryset = queryset.filter(date=date)

        if message:
            queryset = queryset.filter(message__icontains=message)

        if priority:
            queryset = queryset.filter(priority=priority)

        return queryset




class ReminderDeleteView(generics.DestroyAPIView):
    serializer_class = ReminderSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reminder.objects.filter(user=self.request.user)


class ReminderUpdateView(generics.UpdateAPIView):
    serializer_class = ReminderSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reminder.objects.filter(user=self.request.user)