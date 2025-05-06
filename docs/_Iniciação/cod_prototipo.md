```
@startuml
left to right direction
actor "Agente de Censo" as Agente
actor "Administrador" as Admin

rectangle "Aplicativo Censo Primeira" {
    
    Agente --> (Realizar Login)
    Agente --> (Cadastrar Morador)
    Agente --> (Preencher Formulário Demográfico)
    Agente --> (Coletar Localização)
    Agente --> (Salvar Dados Offline)
    
    Admin --> (Acessar Painel de Dados)
    Admin --> (Gerar Relatórios)
    Admin --> (Exportar Dados)
    Admin --> (Gerenciar Usuários)
    
    (Cadastrar Morador) --> (Validar Dados)
    (Salvar Dados Offline) --> (Sincronizar com Servidor)
}

@enduml
```
