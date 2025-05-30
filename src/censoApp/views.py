from django.shortcuts import render

from rest_framework import viewsets
from censoApp.models import Domicilio, Morador, Falecimento, Religiao, Rua, Informante, Contato, Trabalho, Deslocamento
from censoApp.serializers import RuaSerializer, MoradorSerializer, DomicilioSerializer, FalecimentoSerializer, ReligiaoSerializer, InformanteCivilSerializer, ContatoSerializer, TrabalhoSerializer, DeslocamentoSerializer

class RuaViewSet(viewsets.ModelViewSet):
    queryset = Rua.objects.all()
    serializer_class = RuaSerializer

class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer

class DomicilioViewSet(viewsets.ModelViewSet):
    queryset = Domicilio.objects.all()
    serializer_class = DomicilioSerializer

class FalecimentoViewSet(viewsets.ModelViewSet):
    queryset = Falecimento.objects.all()
    serializer_class = FalecimentoSerializer

class ReligiaoViewSet(viewsets.ModelViewSet):
    queryset = Religiao.objects.all()
    serializer_class = ReligiaoSerializer

class InformanteCivilViewSet(viewsets.ModelViewSet):
    queryset = Informante.objects.all()
    serializer_class = InformanteCivilSerializer

class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

class TrabalhoViewSet(viewsets.ModelViewSet):
    queryset = Trabalho.objects.all()
    serializer_class = TrabalhoSerializer

class DeslocamentoViewSet(viewsets.ModelViewSet):
    queryset = Deslocamento.objects.all()
    serializer_class = DeslocamentoSerializer

