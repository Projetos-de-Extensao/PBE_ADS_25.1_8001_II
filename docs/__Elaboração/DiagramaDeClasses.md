@startuml
' Título do Diagrama
title Diagrama de Classes - Questionário Básico Censo Ilha Primeira

' CLASSES PRINCIPAIS
class Domicilio {
  - uf: String
  - municipio: String
  - distrito: String
  - subdistrito: String
  - setor: String
  - tipoDomicilio: TipoDomicilio
  - tipoConstrucao: TipoConstrucao
  - abastecimentoAgua: FormaAgua
  - destinoLixo: DestinoLixo
  - numeroBanheiros: int
  - esgoto: String
}

class Morador {
  - nome: String
  - sobrenome: String
  - sexo: Sexo
  - dataNascimento: Date
  - parentesco: Parentesco
  - corRaca: CorRaca
  - falaPortugues: SimNao
  - consideraIndigena: SimNao
  - consideraQuilombola: SimNao
  - etnia1: String
  - etnia2: String
  - falaLinguaIndigena: SimNao
  - lingua1: String
  - lingua2: String
  - lingua3: String
  - sabeLerEscrever: SimNao
}

class Rendimento {
  - valor: float
  - faixa: String
  - tipo: String
}

class Mortalidade {
  - nome: String
  - sobrenome: String
  - sexo: Sexo
  - idadeAnos: int
  - idadeMeses: int
  - dataFalecimento: Date
}

class PrestadorInformacao {
  - quemPrestou: String
  - nomeOutroMorador: String
}

class RegistroCivil {
  - tipoRegistro: String
}

class Contato {
  - nome: String
  - email: String
  - telefone: String
  - cpf: String
}

' RELACIONAMENTOS
Domicilio "1" -- "0..*" Morador
Domicilio "1" -- "0..*" Mortalidade
Morador "0..1" -- "1" RegistroCivil
Morador "0..1" -- "1" Rendimento
Morador "1" -- "1" PrestadorInformacao
Morador "1" -- "1" Contato

@enduml
