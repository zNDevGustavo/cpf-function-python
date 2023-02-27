"""A"""
from random import randint
def gera_cpf(show=False):
    """Gerador de CPF"""
    # Gera os primeiros 9 dígitos aleatórios para o CPF
    digs = ''
    for i in range(0, 9):
        digs += str(randint(0, 9))
    # Gera os últimos dois dígitos baseados nos primeiros 9
    for cont_dig in range(1, 3):
        soma = 0
        contagem = 10 if cont_dig == 1 else 11
        for i in digs:
            soma += int(i) * contagem
            contagem -= 1
        num_dig = soma * 10 % 11
        num_dig = 0 if num_dig > 9 else num_dig
        digs += (str(num_dig))
    # Checa se o argumento show é verdadeiro para mostrar os pontos e traço
    if show:
        digs = f'{digs[:3]}.{digs[3:6]}.{digs[6:9]}-{digs[9:]}'
    # Retorna o CPF válido com os 11 dígitos.
    return digs

print(gera_cpf(True))
