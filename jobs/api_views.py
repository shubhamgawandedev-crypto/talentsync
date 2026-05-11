from rest_framework import generics
from .models import Job
from .serializers import JobSerializer


class JobListAPIView(generics.ListAPIView):

    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobCreateAPIView(generics.CreateAPIView):

    queryset = Job.objects.all()
    serializer_class = JobSerializer