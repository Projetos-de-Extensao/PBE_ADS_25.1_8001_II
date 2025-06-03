@startuml
skinparam classAttributeIconSize 0

class Domicilio {
  +id: int
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

class Rua {
  +nome: String
}

class Morador {
  +id: int
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
  +possui_deficiencia: String
  +diagnostico_autismo: boolean
  +trabalha: boolean
  +faixa_renda: String
}

class Trabalho {
  +ocupacao: String
  +atividade: String
  +local: String
  +tipo_contrato: String
  +empresa_registrada: boolean
  +infraestrutura: String
  +deslocamento: boolean
  +dificuldades: String
  +rendimento_suficiente: boolean
  +interesse_cursos: boolean
  +trabalho_sazonal: boolean
  +familia_envovida: boolean
  +destino_produto: String
  +acesso_credito: boolean
  +associacoes: String
  +sustentabilidade: String
  +impacto_ambiental: String
  +expansao_futura: boolean
  +integracao_comunidade: boolean
  +melhorias_sugeridas: String
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

class Falecimento {
  +nome: String
  +sobrenome: String
  +sexo: String
  +idade: int
  +data: Date
  +tempo_conclusao: String
}

class Religiao {
  +descricao: String
}

class Contato {
  +nome: String
  +email: String
  +telefone: String
}

class Informante {
  +nome: String
  +relacao_domicilio: String
}

Domicilio "1" -- "0..*" Morador
Domicilio "1" -- "1..*" Rua
Morador "0..1" -- "1" Falecimento
Morador "1" -- "1" Contato
Morador "0..1" -- "1" Trabalho
Morador "0..1" -- "1" Deslocamento
Domicilio "1" -- "1" Religiao
Domicilio "1" -- "1" Informante

@enduml
