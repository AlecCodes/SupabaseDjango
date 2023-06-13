from .models import Snack
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class SnackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snack
        fields = ['id','name','isGood']