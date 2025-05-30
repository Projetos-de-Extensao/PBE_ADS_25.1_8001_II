from enum import Enum
from datetime import date


# ==== ENUMS AUXILIARES ====

class TipoDomicilio(Enum):
    CASA = "Casa"
    APARTAMENTO = "Apartamento"
    OUTRO = "Outro"


class TipoConstrucao(Enum):
    ALVENARIA = "Alvenaria"
    MADEIRA = "Madeira"
    MISTA = "Mista"
    OUTRO = "Outro"


class FormaAgua(Enum):
    REDE_GERAL = "Rede Geral"
    POCO = "Poço"
    NACENTE = "Nascente"
    OUTRO = "Outro"


class DestinoLixo(Enum):
    COLETA = "Coleta"
    QUEIMA = "Queima"
    ENTERRA = "Enterra"
    OUTRO = "Outro"


class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"
    OUTRO = "Outro"


class SimNao(Enum):
    SIM = "Sim"
    NAO = "Não"


class Parentesco(Enum):
    RESPONSAVEL = "Responsável"
    CONJUGE = "Cônjuge"
    FILHO = "Filho"
    OUTRO = "Outro"


class CorRaca(Enum):
    BRANCA = "Branca"
    PRETA = "Preta"
    PARDA = "Parda"
    AMARELA = "Amarela"
    INDIGENA = "Indígena"
    OUTRO = "Outro"


# ==== CLASSES PRINCIPAIS ====

class Domicilio:
    def __init__(self, uf, municipio, distrito, subdistrito, setor,
                 tipo_domicilio, tipo_construcao, abastecimento_agua,
                 destino_lixo, numero_banheiros, esgoto):
        self.uf = uf
        self.municipio = municipio
        self.distrito = distrito
        self.subdistrito = subdistrito
        self.setor = setor
        self.tipo_domicilio = tipo_domicilio
        self.tipo_construcao = tipo_construcao
        self.abastecimento_agua = abastecimento_agua
        self.destino_lixo = destino_lixo
        self.numero_banheiros = numero_banheiros
        self.esgoto = esgoto


class Morador:
    def __init__(self, nome, sobrenome, sexo, data_nascimento, parentesco,
                 cor_raca, fala_portugues, considera_indigena,
                 considera_quilombola, etnia1, etnia2, fala_lingua_indigena,
                 lingua1, lingua2, lingua3, sabe_ler_escrever):
        self.nome = nome
        self.sobrenome = sobrenome
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.parentesco = parentesco
        self.cor_raca = cor_raca
        self.fala_portugues = fala_portugues
        self.considera_indigena = considera_indigena
        self.considera_quilombola = considera_quilombola
        self.etnia1 = etnia1
        self.etnia2 = etnia2
        self.fala_lingua_indigena = fala_lingua_indigena
        self.lingua1 = lingua1
        self.lingua2 = lingua2
        self.lingua3 = lingua3
        self.sabe_ler_escrever = sabe_ler_escrever


class Rendimento:
    def __init__(self, valor, faixa, tipo):
        self.valor = valor
        self.faixa = faixa
        self.tipo = tipo


class Mortalidade:
    def __init__(self, nome, sobrenome, sexo, idade_anos, idade_meses, data_falecimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.sexo = sexo
        self.idade_anos = idade_anos
        self.idade_meses = idade_meses
        self.data_falecimento = data_falecimento


class PrestadorInformacao:
    def __init__(self, quem_prestou, nome_outro_morador):
        self.quem_prestou = quem_prestou
        self.nome_outro_morador = nome_outro_morador


class RegistroCivil:
    def __init__(self, tipo_registro):
        self.tipo_registro = tipo_registro


class Contato:
    def __init__(self, nome, email, telefone, cpf):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf
