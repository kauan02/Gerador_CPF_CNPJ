import random

def gerar_cnpj_formatado():
    base = [random.randint(0, 9) for i in range(8)]
    base += [0, 0, 0, 1]
    
    multiplicadores1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma1 = sum([base[i] * multiplicadores1[i] for i in range(12)])
    resto1 = soma1 % 11
    dig1 = 0 if resto1 < 2 else 11 - resto1
    
    base.append(dig1)
    multiplicadores2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma2 = sum([base[i] * multiplicadores2[i] for i in range(13)])
    resto2 = soma2 % 11
    dig2 = 0 if resto2 < 2 else 11 - resto2
    
    base.append(dig2)
    
    cnpj_formatado = "{}{}.{}{}{}.{}{}{}/{}{}{}{}-{}{}".format(*base)
    
    return cnpj_formatado

cnpj_formatado = gerar_cnpj_formatado()
print(f'O CNPJ gerado foi: {cnpj_formatado}')