from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def home(request):
    return render(request, "index.html")

urlpatterns = [
    path('', home),

    path('admin/', admin.site.urls),
    path('api/reminder/', include('reminderapp.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]