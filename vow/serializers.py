from rest_framework import serializers
from .models import *

class customerserializers(serializers.ModelSerializer):
    classes_std = serializers.CharField(source='classes.std')
    classes_sec = serializers.CharField(source='classes.sec')
    class Meta:
        model = customers
        fields = ('name' ,'classes_std', 'classes_sec', 'phone','pk')