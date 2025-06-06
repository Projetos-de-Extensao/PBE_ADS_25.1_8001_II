@startuml
class Rua {
    +nome: CharField
    +Domicilio: ForeignKey -> Domicilio
}

class Religiao {
    +descricao: CharField
    +Morador: ForeignKey -> Morador
}

class Informante {
    +nome: CharField
    +relacao_domicilio: CharField
    +Domicilio: ForeignKey -> Domicilio
}

class Contato {
    +nome: CharField
    +email: EmailField
    +telefone: CharField
    +Domicilio: ForeignKey -> Domicilio
}

class Domicilio {
    +numero: IntegerField
    +endereco: CharField
    +especie: CharField
    +tipo: CharField (choices)
    +agua: CharField
    +energia: CharField
    +internet: BooleanField
    +maquina_lavar: BooleanField
    +coleta_lixo: CharField
    +comodos: IntegerField
    +dormitorios: IntegerField
    +banheiros_com_chuveiro: IntegerField
    +banheiros_sem_chuveiro: IntegerField
    +condicao_ocupacao: CharField (choices)
    +principais_demandas: TextField
}

class Morador {
    +nome: CharField
    +sobrenome: CharField
    +sexo: CharField (choices)
    +data_nascimento: DateField
    +parentesco: CharField (choices)
    +registro_nascimento: CharField (choices)
    +tem_conjuge: BooleanField
    +nome_conjuge: CharField
    +tipo_uniao: CharField
    +sabe_ler: BooleanField
    +frequenta_escola: CharField
    +curso_frequenta: CharField
    +concluiu_superior: BooleanField
    +possui_deficiencia: TextField
    +diagnostico_autismo: BooleanField
    +trabalha: BooleanField
    +faixa_renda: CharField
    +domicilio: ForeignKey -> Domicilio
}

class Falecimento {
    +data: DateField
    +idade: IntegerField
    +tempo_conclusao: CharField
    +morador: OneToOneField -> Morador
}

class Trabalho {
    +ocupacao: CharField
    +atividade: CharField
    +local: CharField
    +tipo_contrato: CharField
    +empresa_registrada: BooleanField
    +infraestrutura: TextField
    +deslocamento: BooleanField
    +dificuldades: TextField
    +rendimento_suficiente: BooleanField
    +interesse_cursos: BooleanField
    +trabalho_sazonal: BooleanField
    +familia_envovida: BooleanField
    +destino_produto: CharField
    +acesso_credito: BooleanField
    +associacoes: TextField
    +sustentabilidade: TextField
    +impacto_ambiental: TextField
    +expansao_futura: BooleanField
    +integracao_comunidade: BooleanField
    +melhorias_sugeridas: TextField
    +morador: OneToOneField -> Morador
}

class Deslocamento {
    +local_trabalho: CharField
    +estado: CharField
    +municipio: CharField
    +pais: CharField
    +retorna_casa: BooleanField
    +tempo_horas: IntegerField
    +tempo_minutos: IntegerField
    +meio_transporte: CharField
    +morador: OneToOneField -> Morador
}

Domicilio "1" -- "many" Morador
Domicilio "1" -- "1" Rua
Domicilio "1" -- "1" Informante
Domicilio "1" -- "many" Contato
Morador "1" -- "1" Falecimento
Morador "1" -- "1" Trabalho
Morador "1" -- "1" Deslocamento
Morador "1" -- "many" Religiao
@enduml
