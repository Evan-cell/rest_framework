from rest_framework import serializers
from .models import languages


class languagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = languages
        fields = '__all__'