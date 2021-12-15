from django.shortcuts import render
from rest_framework import viewsets
from .models import languages
from .serializers import languagesSerializer
# Create your views here.\
class languageView(viewsets.ModelViewSet):
    queryset = languages.objects.all()
    serializer_class = languagesSerializer
