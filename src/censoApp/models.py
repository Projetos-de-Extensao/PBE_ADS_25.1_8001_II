from django.db import models


# ==== ENUMS COMO TUPLAS ==== #

TIPO_DOMICILIO_CHOICES = [
    ("Casa", "Casa"),
    ("Apartamento", "Apartamento"),
    ("Outro", "Outro"),
]

TIPO_CONSTRUCAO_CHOICES = [
    ("Alvenaria", "Alvenaria"),
    ("Madeira", "Madeira"),
    ("Mista", "Mista"),
    ("Outro", "Outro"),
]

FORMA_AGUA_CHOICES = [
    ("Rede Geral", "Rede Geral"),
    ("Poço", "Poço"),
    ("Nascente", "Nascente"),
    ("Outro", "Outro"),
]

DESTINO_LIXO_CHOICES = [
    ("Coleta", "Coleta"),
    ("Queima", "Queima"),
    ("Enterra", "Enterra"),
    ("Outro", "Outro"),
]

SEXO_CHOICES = [
    ("Masculino", "Masculino"),
    ("Feminino", "Feminino"),
    ("Outro", "Outro"),
]

SIM_NAO_CHOICES = [
    ("Sim", "Sim"),
    ("Não", "Não"),
]

PARENTESCO_CHOICES = [
    ("Responsável", "Responsável"),
    ("Cônjuge", "Cônjuge"),
    ("Filho", "Filho"),
    ("Outro", "Outro"),
]

COR_RACA_CHOICES = [
    ("Branca", "Branca"),
    ("Preta", "Preta"),
    ("Parda", "Parda"),
    ("Amarela", "Amarela"),
    ("Indígena", "Indígena"),
    ("Outro", "Outro"),
]


# ==== MODELOS ==== #

class Domicilio(models.Model):
    uf = models.CharField(max_length=2)
    municipio = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)
    subdistrito = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    tipo_domicilio = models.CharField(max_length=20, choices=TIPO_DOMICILIO_CHOICES)
    tipo_construcao = models.CharField(max_length=20, choices=TIPO_CONSTRUCAO_CHOICES)
    abastecimento_agua = models.CharField(max_length=20, choices=FORMA_AGUA_CHOICES)
    destino_lixo = models.CharField(max_length=20, choices=DESTINO_LIXO_CHOICES)
    numero_banheiros = models.IntegerField()
    esgoto = models.CharField(max_length=3, choices=SIM_NAO_CHOICES)


class Morador(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    data_nascimento = models.DateField()
    parentesco = models.CharField(max_length=20, choices=PARENTESCO_CHOICES)
    cor_raca = models.CharField(max_length=20, choices=COR_RACA_CHOICES)
    fala_portugues = models.CharField(max_length=3, choices=SIM_NAO_CHOICES)
    considera_indigena = models.CharField(max_length=3, choices=SIM_NAO_CHOICES)
    considera_quilombola = models.CharField(max_length=3, choices=SIM_NAO_CHOICES)
    etnia1 = models.CharField(max_length=100, blank=True, null=True)
    etnia2 = models.CharField(max_length=100, blank=True, null=True)
    fala_lingua_indigena = models.CharField(max_length=3, choices=SIM_NAO_CHOICES)
    lingua1 = models.CharField(max_length=100, blank=True, null=True)
    lingua2 = models.CharField(max_length=100, blank=True, null=True)
    lingua3 = models.CharField(max_length=100, blank=True, null=True)
    sabe_ler_escrever = models.CharField(max_length=3, choices=SIM_NAO_CHOICES)


class Rendimento(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    faixa = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)


class Mortalidade(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    idade_anos = models.IntegerField()
    idade_meses = models.IntegerField()
    data_falecimento = models.DateField()


class PrestadorInformacao(models.Model):
    quem_prestou = models.CharField(max_length=100)
    nome_outro_morador = models.CharField(max_length=100, blank=True, null=True)


class RegistroCivil(models.Model):
    tipo_registro = models.CharField(max_length=100)


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
