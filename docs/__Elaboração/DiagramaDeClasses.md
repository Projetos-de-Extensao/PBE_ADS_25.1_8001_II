@startuml
skinparam classAttributeIconSize 0

class Rua {
  +nome: String
}

class Religiao {
  +descricao: String
}

class Informante {
  +nome: String
  +relacao_domicilio: String
}

class Contato {
  +nome: String
  +email: String
  +telefone: String
}

class Domicilio {
  +numero: int
  +endereco: String
  +especie: String
  +tipo: String
  +agua: String
  +energia: String
  +internet: boolean
  +maquina_lavar: boolean
  +coleta_lixo: String
  +comodos: int
  +dormitorios: int
  +banheiros_com_chuveiro: int
  +banheiros_sem_chuveiro: int
  +condicao_ocupacao: String
  +principais_demandas: String
}

class Morador {
  +nome: String
  +sobrenome: String
  +sexo: String
  +data_nascimento: Date
  +parentesco: String
  +registro_nascimento: String
  +tem_conjuge: boolean
  +nome_conjuge: String
  +tipo_uniao: String
  +sabe_ler: boolean
  +frequenta_escola: String
  +curso_frequenta: String
  +concluiu_superior: boolean
  +possui_deficiencia: Text
  +diagnostico_autismo: boolean
  +trabalha: boolean
  +faixa_renda: String
}

class Falecimento {
  +data: Date
  +idade: int
  +tempo_conclusao: String
}

class Trabalho {
  +ocupacao: String
  +atividade: String
  +local: String
  +tipo_contrato: String
  +empresa_registrada: boolean
  +infraestrutura: Text
  +deslocamento: boolean
  +dificuldades: Text
  +rendimento_suficiente: boolean
  +interesse_cursos: boolean
  +trabalho_sazonal: boolean
  +familia_envovida: boolean
  +destino_produto: String
  +acesso_credito: boolean
  +associacoes: Text
  +sustentabilidade: Text
  +impacto_ambiental: Text
  +expansao_futura: boolean
  +integracao_comunidade: boolean
  +melhorias_sugeridas: Text
}

class Deslocamento {
  +local_trabalho: String
  +estado: String
  +municipio: String
  +pais: String
  +retorna_casa: boolean
  +tempo_horas: int
  +tempo_minutos: int
  +meio_transporte: String
}

' Relacionamentos
Domicilio --> "0..1" Rua
Domicilio --> "0..1" Religiao
Domicilio --> "0..1" Informante
Morador --> "1" Domicilio
Morador --> "0..1" Contato
Falecimento --> "1" Morador
Trabalho --> "1" Morador
Deslocamento --> "1" Morador
@enduml
