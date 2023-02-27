"""Gerador de CPF"""
from random import randint
def gen_cpf(show=False):
    """Função gerador de CPF"""
    # Gera os primeiros 9 dígitos aleatórios para o CPF
    digs = ''
    for i in range(0, 9):
        digs += str(randint(0, 9))
    # Gera os últimos dois dígitos baseados nos primeiros 9
    for count_dig in range(1, 3):
        sum_digs = 0
        count = 10 if count_dig == 1 else 11
        for i in digs:
            sum_digs += int(i) * count
            count -= 1
        num_dig = sum_digs * 10 % 11
        num_dig = 0 if num_dig > 9 else num_dig
        digs += (str(num_dig))
    # Checa se o argumento show é verdadeiro para mostrar os pontos e traços
    if show:
        digs = f'{digs[:3]}.{digs[3:6]}.{digs[6:9]}-{digs[9:]}'
    # Retorna o CPF válido com os 11 dígitos.
    return digs

print(gen_cpf(True))
