from django.shortcuts import render
from .models import Snack
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SnackSerializer 


# Create your views here.
from .models import Snack 
class TodoViewSets(viewsets.ModelViewSet):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = [permissions.AllowAny]
