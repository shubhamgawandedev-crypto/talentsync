from rest_framework import generics
from .models import Application
from .serializers import ApplicationSerializer


class ApplicationListAPIView(generics.ListAPIView):

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationCreateAPIView(generics.CreateAPIView):

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer