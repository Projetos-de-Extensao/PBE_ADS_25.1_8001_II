from django.shortcuts import render

from rest_framework import viewsets
from censoApp.models import Domicilio, Morador, Rendimento, Mortalidade, PrestadorInformacao, RegistroCivil, Contato
from censoApp.serializers import DomicilioSerializer, MoradorSerializer, RendimentoSerializer, MortalidadeSerializer, PrestadorInformacaoSerializer, RegistroCivilSerializer, ContatoSerializer

class DomicilioViewSet(viewsets.ModelViewSet):
    queryset = Domicilio.objects.all()
    serializer_class = DomicilioSerializer

class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer

class RendimentoViewSet(viewsets.ModelViewSet):
    queryset = Rendimento.objects.all()
    serializer_class = RendimentoSerializer

class MortalidadeViewSet(viewsets.ModelViewSet):
    queryset = Mortalidade.objects.all()
    serializer_class = MortalidadeSerializer

class PrestadorInformacaoViewSet(viewsets.ModelViewSet):
    queryset = PrestadorInformacao.objects.all()
    serializer_class = PrestadorInformacaoSerializer

class RegistroCivilViewSet(viewsets.ModelViewSet):
    queryset = RegistroCivil.objects.all()
    serializer_class = RegistroCivilSerializer

class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer