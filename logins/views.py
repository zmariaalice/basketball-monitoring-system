from rest_framework import generics
from .models import Login
from .serializers import LoginSerializer

class LoginListCreateView(generics.ListCreateAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class LoginDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
