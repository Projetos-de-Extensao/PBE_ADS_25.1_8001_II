from rest_framework import serializers
from censoApp.models import Morador
from censoApp.models import Domicilio
from censoApp.models import Mortalidade
from censoApp.models import Rendimento
from censoApp.models import PrestadorInformacao
from censoApp.models import RegistroCivil
from censoApp.models import Contato


class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = '__all__'

class DomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domicilio
        fields = '__all__'

class MortalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mortalidade
        fields = '__all__'

class RendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rendimento
        fields = '__all__'

class PrestadorInformacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrestadorInformacao
        fields = '__all__'

class RegistroCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroCivil
        fields = '__all__'

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'