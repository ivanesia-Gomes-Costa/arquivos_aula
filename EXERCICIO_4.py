# EXERCICIO 04


indice = []


def cadastra_produto(produto_para_cadastrar: dict):
    indice.append(produto_para_cadastrar)
    return


opcao = int(input('Deseja realizar um cadastro ? 0 - Não     1 - Sim '))
while opcao == 1:
    produto_novo = {}

    produto_novo['codigo'] = int(input('Qual o código do produto: '))

    if produto_novo['codigo'] == 0:
        print('Código 0, Cadastro finalizado.')
        break

    produto_novo['estoque'] = int(input('Digite a quantidade em estoque: '))
    produto_novo['minimo'] = int(input('Digite a quantidade mínima do estoque: '))

    cadastra_produto(produto_novo)
    opcao = int(input('Novo produto? 0 - Não     1 - Sim '))

if len(indice) > 0:
    print('Produtos por código em ordem crescente:')
    print("Código".center(10), end='')
    print("Estoque".center(10), end='')
    print("Mínimo".center(10))

    for produto in sorted(indice, key=lambda item: item['codigo']):
        print(str(produto['codigo']).center(10), end='')
        print(str(produto['estoque']).center(10), end='')
        print(str(produto['minimo']).center(10))
else:
    print('Sem conteúdo.')