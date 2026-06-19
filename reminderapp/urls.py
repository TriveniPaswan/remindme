from django.urls import path
from .views import (
    RegisterView,
    ReminderListCreateView,
    ReminderDeleteView,
    ReminderUpdateView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

    path('', ReminderListCreateView.as_view(), name='reminder-list'),
    path('delete/<int:pk>/', ReminderDeleteView.as_view(), name='reminder-delete'),
    path('update/<int:pk>/', ReminderUpdateView.as_view(), name='reminder-update'),
]