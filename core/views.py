from django.shortcuts import render
from rest_framework import generics
from core.models import Details
from .serializers import DetailsSerializers

# Create your views here.
class ListDetails(generics.ListCreateAPIView):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializers