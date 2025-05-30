from rest_framework import serializers
from censoApp.models import Deslocamento
from censoApp.models import Trabalho
from censoApp.models import Domicilio
from censoApp.models import Falecimento
from censoApp.models import Morador
from censoApp.models import Informante
from censoApp.models import Rua
from censoApp.models import Religiao
from censoApp.models import Contato


class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = '__all__'

class DomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domicilio
        fields = '__all__'

class FalecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Falecimento
        fields = '__all__'

class ReligiaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religiao
        fields = '__all__'

class RuaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rua
        fields = '__all__'

class InformanteCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informante
        fields = '__all__'

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'

class TrabalhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabalho
        fields = '__all__'

class DeslocamentoSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Deslocamento
        fields = '__all__'