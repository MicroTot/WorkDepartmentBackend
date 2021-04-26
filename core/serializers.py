from rest_framework import serializers
from .models import Details

class DetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = "__all__"