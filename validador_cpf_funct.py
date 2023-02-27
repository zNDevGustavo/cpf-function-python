"""Validador de CPF"""
def valida_cpf(cpf):
    """Validador de CPF"""
    # Remove pontos e traços
    cpf = cpf.strip().replace('-', '').replace('.', '')
    # Verifica se tem apenas números
    for i in cpf:
        if i.isalpha():
            return 'CPF Inválido! Digite apenas números.'
    if cpf[0]*11 == cpf:
        return 'CPF Inválido!'
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) < 11:
        return 'CPF Inválido! O CPF deve ter 11 dígitos.'
    # Verifica os dois dígitos
    digs = ''
    for cont_dig in range(1, 3):
        soma = 0
        contagem = 10 if cont_dig == 1 else 11
        for i in cpf[:contagem-1]:
            soma += int(i) * contagem
            contagem -= 1
        num_dig = soma * 10 % 11
        num_dig = 0 if num_dig > 9 else num_dig
        digs += (str(num_dig))
    if cpf[-2] == digs[0] and cpf[-1] == digs[1]:
        return 'CPF Válido!'
    return 'CPF Inválido!'


CPF_INPUT = str(input('CPF: '))
print(valida_cpf(CPF_INPUT))
