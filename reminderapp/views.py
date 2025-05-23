# from django.http import HttpResponse
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import ReminderSerializer

# # Simple homepage view
# def home(request):
#     return HttpResponse("Reminder app ka homepage!")

# # API endpoint to create reminder
# class ReminderCreateView(APIView):
#     def post(self, request):
#         serializer = ReminderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Reminder app ka homepage!")
# reminderapp/views.py
from rest_framework import generics
from .models import Reminder
from .serializers import ReminderSerializer

class ReminderListCreateView(generics.ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
