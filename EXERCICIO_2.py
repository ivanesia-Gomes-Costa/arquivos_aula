""""
Faça uma função que receba o nome e sobrenome de uma pessoa e retorne a 
primeira letra de seu nome e seu sobrenome concatenando com a string
@algoritmos.com.br. No algoritmo principal deverá ser apresentada a mensagem 
ao usuário contendo seu nome completo e seu email
"""
def usuario(nome:str, sobrenome:str):
    if len(nome) > 0 and len(sobrenome) > 0:
        return "Srª" + nome + " " + sobrenome + " " + "seu e-mail e:" + " "+ nome[0].lower() + sobrenome.lower() + "@algoritmo.com.br"
    else:
        return None

print(usuario('ivanesia', 'gomes'))


