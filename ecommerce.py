#1a Cadastrar Produto
#Parametros: catalogo, nome do produto, valor, quantidade
#Exemplos depois e cadastrado
#[['Camiseta Azul', 89.90, 50], ['Cachecol', 35.00, 30]]
nome = 0
preco = 1
estoque = 2


def cadastrar_produto(catalogo:list[list [object]],
                       nome:str, preco:float, estoque:int) -> list[list[object]]:
    """Cadastra um produto em um catalogo
    
    Params: 
    :Catalogo lista de produtos
    :Nome nome do produto
    :Preco preco do produto
    :Estoque quantidade de estoque

    Returns: Lista de produtos cadastrados"""
    
    catalogo.append([nome, preco, estoque])
    return catalogo

#2a funcao
#Exibir o que esta no catalogo
#Exemplo: Camiseta Azul - R$89.90 (estoque: 50)


def exibir_catalogo(catalogo:list[list[object]]) -> None:
    for produto in catalogo:
        print(f'{produto[nome]} - R${produto[preco]} (estoque:{produto[estoque]})')

loja = [['Guitarra', 1199.90, 5,], ['Baixo', 1599.90, 8]]
exibir_catalogo(loja)

loja = []
produto = input('Digite o nome do produto: ')
valor = float(input('Digite o valor do produto: '))
estoque = int(input('Digite a quantidade de produtos: '))
cadastrar_produto(loja, produto, valor, estoque)