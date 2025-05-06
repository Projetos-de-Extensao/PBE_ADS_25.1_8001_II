@startuml

actor "Cliente" as Cliente
actor "Entregador" as Entregador
actor "Administrador" as Administrador

usecase "Fazer o pedido" as UC2
usecase "Acompanhar status do pedido" as UC3
usecase "Realizar entrega" as UC4
usecase "Gerenciar pedidos" as UC6
usecase "Gerenciar encomendas" as UC7

Cliente -- UC2
Cliente -- UC3

Entregador -- UC4

Administrador -- UC6
Administrador -- UC7

@enduml
