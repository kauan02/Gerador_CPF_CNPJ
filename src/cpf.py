import random

def gerar_cpf_formatado():
    uf = {
        "RS": 0,
        "DF": 1, "GO": 1, "MT": 1, "MS": 1, "TO": 1,
        "AM": 2, "PA": 2, "RR": 2, "AP": 2, "AC": 2, "RO": 2,
        "CE": 3, "MA": 3, "PI": 3,
        "PE": 4, "RN": 4, "PB": 4, "AL": 4,
        "BA": 5, "SE": 5,
        "MG": 6,
        "RJ": 7, "ES": 7,
        "SP": 8,
        "PR": 9, "SC": 9
    }
    
    estado = input("Base gerada, qual o estado de emissao? ex: SP\n").strip().upper()
    
    if estado not in uf:
        return "Estado invalido"
    
    base = [random.randint(0, 9) for n in range(8)]
    base.append(uf[estado])
    
    soma1 = sum([(10 - i) * base[i] for i in range(9)])
    dig1 = (soma1 * 10 % 11) % 10
    
    soma2 = sum([(11 - i) * base[i] for i in range(9)] + [2 * dig1])
    dig2 = (soma2 * 10 % 11) % 10
    
    cpf = base + [dig1, dig2]
    
    cpf_str = "".join(map(str, cpf))
    cpf_formatado = f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"
    
    return cpf_formatado, cpf

print(gerar_cpf_formatado())