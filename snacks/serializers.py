from .models import Snack
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class SnackSerializer(serializers.HyperlinkedModelSerializer):
    def get_isGood(self, obj):
        return obj.isGood
    
    class Meta:
        model = Snack
        fields = ['id','name','isgood']