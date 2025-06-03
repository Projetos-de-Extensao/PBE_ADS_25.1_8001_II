from django.db import models


SEXO_CHOICES = [
    ('masculino', 'Masculino'),
    ('feminino', 'Feminino'),
    ('outro', 'Outro'),
]

PARENTESCO_CHOICES = [
    ('responsavel', 'Pessoa responsável pelo domicílio'),
    ('conjuge_dif', 'Cônjuge ou companheiro(a) de sexo diferente'),
    ('conjuge_mesmo', 'Cônjuge ou companheiro(a) do mesmo sexo'),
    ('filho_comum', 'Filho(a) do responsável e do cônjuge'),
    ('filho_resp', 'Filho(a) somente do responsável'),
    ('genro_nora', 'Genro ou nora'),
    ('pai_mae', 'Pai, mãe, padrasto ou madrasta'),
    ('sogro', 'Sogro(a)'),
    ('neto', 'Neto(a)'),
    ('enteado', 'Enteado(a)'),
    ('irmao', 'Irmão ou irmã'),
    ('avo', 'Avô ou avó'),
    ('outro', 'Outro parente'),
    ('agregado', 'Agregado(a)'),
    ('bisneto', 'Bisneto(a)'),
    ('pensionista', 'Pensionista'),
    ('empregado_dom', 'Empregado(a) doméstico(a)'),
    ('parente_empregado', 'Parente do(a) empregado(a) doméstico(a)'),
    ('individual', 'Individual em domicílio coletivo'),
]

REGISTRO_NASCIMENTO_CHOICES = [
    ('cartorio', 'Do cartório'),
    ('indigena', 'Registro administrativo indígena'),
    ('nao_tem', 'Não tem'),
    ('nao_sabe', 'Não sabe'),
]

CONDICAO_OCUPACAO_CHOICES = [
    ('ainda_pagando', 'Ainda pagando'),
    ('alugado', 'Alugado'),
    ('empregador', 'Por empregador'),
    ('familiar', 'Por familiar'),
    ('outra', 'Outra forma'),
    ('pago', 'Já pago, herdado ou ganho'),
]

TIPO_DOMICILIO_CHOICES = [
    ('casa', 'Casa'),
    ('vila_condominio', 'Casa de vila ou condomínio'),
    ('cortico', 'Cortiço'),
    ('inacabado', 'Estrutura degradada/inacabada'),
    ('asilo', 'Asilo ou instituição'),
    ('hotel', 'Hotel ou pensão'),
    ('alojamento', 'Alojamento'),
    ('outros', 'Outros'),
]
TIPO_RELIGIAO_CHOICES = [
    ('catolica', 'Católica'),
    ('evangelica', 'Evangélica'),
    ('espirita', 'Espírita'),
    ('umbanda', 'Umbanda'),
    ('candomble', 'Candomblé'),
    ('islamica', 'Islâmica'),
    ('budista', 'Budista'),
    ('judaica', 'Judaica'),
    ('hindu', 'Hindu'),
    ('ateu', 'Ateu'),
    ('agnostico', 'Agnóstico'),
    ('outra', 'Outra religião'),
]
TIPO_RUA_CHOICES = [
    ('asfalto', 'Asfalto'),
    ('paralelepipedo', 'Paralelepípedo'),
    ('terra', 'Terra'),
    ('outro', 'Outro tipo de rua'),
]
TIPO_INFORMANTE_CHOICES = [
    ('responsavel', 'Responsável pelo domicílio'),
    ('conjuge', 'Cônjuge ou companheiro(a)'),
    ('filho', 'Filho(a) do responsável'),
    ('outro', 'Outro parente ou agregado'),
]

# ==== MODELOS ==== #

class Rua(models.Model):
    nome = models.CharField(max_length=100, choices=TIPO_RUA_CHOICES, null=False, blank=False)

    def __str__(self):
        return self.nome


class Religiao(models.Model):
    descricao = models.CharField(max_length=100, choices=TIPO_RELIGIAO_CHOICES, null=False, blank=False)

    def __str__(self):
        return self.descricao


class Informante(models.Model):
    nome = models.CharField(max_length=100, choices=TIPO_INFORMANTE_CHOICES, null=False, blank=False)
    relacao_domicilio = models.CharField(max_length=100, null=False, blank=False)


class Contato(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    telefone = models.CharField(max_length=20, null=False, blank=False)


class Domicilio(models.Model):
    numero = models.IntegerField(null=False, blank=False)
    endereco = models.CharField(max_length=255, null=False, blank=False)
    rua = models.ForeignKey(Rua, on_delete=models.SET_NULL, null=True, blank=True)
    especie = models.CharField(max_length=100, null=False, blank=False)
    tipo = models.CharField(max_length=30, choices=TIPO_DOMICILIO_CHOICES, null=False, blank=False)
    agua = models.CharField(max_length=100, null=False, blank=False)
    energia = models.CharField(max_length=100, null=False, blank=False)
    internet = models.BooleanField(null=False, blank=False)
    maquina_lavar = models.BooleanField(null=False, blank=False)
    coleta_lixo = models.CharField(max_length=255, null=True, blank=True)
    comodos = models.IntegerField(null=False, blank=False)
    dormitorios = models.IntegerField(null=False, blank=False)
    banheiros_com_chuveiro = models.IntegerField(null=True, blank=True)
    banheiros_sem_chuveiro = models.IntegerField(null=False, blank=False)
    condicao_ocupacao = models.CharField(max_length=30, choices=CONDICAO_OCUPACAO_CHOICES, null=False, blank=False)
    principais_demandas = models.TextField(null=False, blank=False)
    religiao = models.ForeignKey(Religiao, on_delete=models.SET_NULL, null=True, blank=True)
    informante = models.OneToOneField(Informante, on_delete=models.SET_NULL, null=True, blank=True)


class Morador(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    sobrenome = models.CharField(max_length=100, null=False, blank=False)
    sexo = models.CharField(max_length=15, choices=SEXO_CHOICES, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    parentesco = models.CharField(max_length=30, choices=PARENTESCO_CHOICES, null=False, blank=False)
    registro_nascimento = models.CharField(max_length=20, choices=REGISTRO_NASCIMENTO_CHOICES, null=False, blank=False)
    tem_conjuge = models.BooleanField(null=False, blank=False)
    nome_conjuge = models.CharField(max_length=100, null=True, blank=True)
    tipo_uniao = models.CharField(max_length=100, null=True, blank=True)
    sabe_ler = models.BooleanField(null=False, blank=False)
    frequenta_escola = models.CharField(max_length=30, null=False, blank=False)
    curso_frequenta = models.CharField(max_length=100, null=False, blank=False)
    concluiu_superior = models.BooleanField(null=False, blank=False)
    possui_deficiencia = models.TextField(null=True, blank=True)
    diagnostico_autismo = models.BooleanField(null=False, blank=False)
    trabalha = models.BooleanField(null=False, blank=False)
    faixa_renda = models.CharField(max_length=50, null=False, blank=False)
    contato = models.OneToOneField(Contato, on_delete=models.SET_NULL, null=True, blank=True)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE, null=False, blank=False)


class Falecimento(models.Model):
    morador = models.OneToOneField(Morador, on_delete=models.CASCADE, null=False, blank=False)
    data = models.DateField(null=False, blank=False)
    idade = models.IntegerField(null=False, blank=False)
    tempo_conclusao = models.CharField(max_length=100, null=False, blank=False)


class Trabalho(models.Model):
    morador = models.OneToOneField(Morador, on_delete=models.CASCADE, null=False, blank=False)
    ocupacao = models.CharField(max_length=100, null=False, blank=False)
    atividade = models.CharField(max_length=100, null=False, blank=False)
    local = models.CharField(max_length=100, null=False, blank=False)
    tipo_contrato = models.CharField(max_length=100, null=False, blank=False)
    empresa_registrada = models.BooleanField(null=False, blank=False)
    infraestrutura = models.TextField(null=False, blank=False)
    deslocamento = models.BooleanField(null=False, blank=False)
    dificuldades = models.TextField(null=False, blank=False)
    rendimento_suficiente = models.BooleanField(null=False, blank=False)
    interesse_cursos = models.BooleanField(null=False, blank=False)
    trabalho_sazonal = models.BooleanField(null=False, blank=False)
    familia_envovida = models.BooleanField(null=False, blank=False)
    destino_produto = models.CharField(max_length=100, null=False, blank=False)
    acesso_credito = models.BooleanField(null=False, blank=False)
    associacoes = models.TextField(null=False, blank=False)
    sustentabilidade = models.TextField(null=False, blank=False)
    impacto_ambiental = models.TextField(null=False, blank=False)
    expansao_futura = models.BooleanField(null=False, blank=False)
    integracao_comunidade = models.BooleanField(null=False, blank=False)
    melhorias_sugeridas = models.TextField(null=False, blank=False)


class Deslocamento(models.Model):
    morador = models.OneToOneField(Morador, on_delete=models.CASCADE, null=False, blank=False)
    local_trabalho = models.CharField(max_length=100, null=False, blank=False)
    estado = models.CharField(max_length=100, null=False, blank=False)
    municipio = models.CharField(max_length=100, null=False, blank=False)
    pais = models.CharField(max_length=100, null=False, blank=False)
    retorna_casa = models.BooleanField(null=False, blank=False)
    tempo_horas = models.IntegerField(null=False, blank=False)
    tempo_minutos = models.IntegerField(null=False, blank=False)
    meio_transporte = models.CharField(max_length=100, null=False, blank=False)
