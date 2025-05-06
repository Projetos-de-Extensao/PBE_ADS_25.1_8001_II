@startuml

class Cliente {
    -id: int
    -nome: string
    -endereco: string
    -telefone: string
    +fazerPedidoEncomenda(): Encomenda
    +acompanharStatus(): string
}

class Entregador {
    -id: int
    -nome: string
    -telefone: string
    +realizarEntrega(): void
}

class Encomenda {
    -id: int
    -dataPedido: Date
    -status: string
    -cliente: Cliente
    -itens: List<ItemEncomenda>
    +atualizarStatus(status: string): void
}

class ItemEncomenda {
    -id: int
    -descricao: string
    -peso: double
    +calcularFrete(): double
}

class Administrador {
    -id: int
    -nome: string
    -telefone: string
    +gerenciarEncomendas(): void
    +registrarProduto(): void
}

class Produto {
    -id: int
    -nome: string
    -descricao: string
    -preco: double
}

class Pedido {
    -id: int
    -data: Date
    -status: string
    +atualizarStatus(status: string): void
}

Cliente "1" -- "*" Encomenda
Encomenda "1" -- "*" ItemEncomenda
Administrador "1" -- "*" Produto
Administrador "1" -- "*" Encomenda

@enduml
