@startuml

actor "Cliente" as Cliente
actor "Entregador" as Entregador
actor "Administrador" as Administrador

usecase "Fazer Pedido de Comida" as UC1
usecase "Fazer Pedido de Encomenda" as UC2
usecase "Acompanhar Status do Pedido" as UC3
usecase "Realizar Entrega" as UC4
usecase "Registrar Novo Produto/Comida" as UC5
usecase "Gerenciar Pedidos" as UC6
usecase "Gerenciar Encomendas" as UC7

Cliente -- UC1
Cliente -- UC2
Cliente -- UC3

Entregador -- UC4

Administrador -- UC5
Administrador -- UC6
Administrador -- UC7

@enduml
