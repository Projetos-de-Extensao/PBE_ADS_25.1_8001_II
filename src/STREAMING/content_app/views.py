from django.shortcuts import render

from rest_framework import viewsets
from .models import Content
from .serializers import ContentSerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
       serializer.save(creator=self.request.user)
