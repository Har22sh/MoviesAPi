from rest_framework import serializers
from .models import *

class MoviesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesData
        fields =["id","title",'rating','genres','update_at','create_at']
        # '__all__'
