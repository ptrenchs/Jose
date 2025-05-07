def numeros_primos_valor(val):
    num = 3
    numeros_primos = [2]
    while num <= val:
        for num_p in numeros_primos:
            if num % num_p == 0:
                break
        if num % num_p != 0:
            numeros_primos.append(num)
        num += 1
    return [1] + numeros_primos

def descomponer_facotres(*valor):
    for val in valor:
        _val = val
        print(f'Descomposicio factors del numero {val}')
        numeros_primos = numeros_primos_valor(val)[::-1][:-1]
        for num_p in numeros_primos:
            while True:
                if _val % num_p == 0:
                    print(f'{int(_val)}|{num_p}')
                    _val = _val / num_p
                    
                else:
                    break
        print(f'{int(_val)}|\n')

def minim_comu_multiple(*valor):
    if len(valor) < 2:
        print('Inserte mas de dos valores separados por el caracter ","')
        return None
    dic_num = {}
    for val in valor:
        _val = val
        print(f'Descomposicio factors del numero {val}')
        numeros_primos = numeros_primos_valor(val)[::-1][:-1]
        
        for num_p in numeros_primos:
            contar = 0
            while True:
                if _val % num_p == 0:
                    print(f'{int(_val)}|{num_p}')
                    _val = _val / num_p
                    contar +=1
                else:
                    break
            try:
                if dic_num[num_p] < contar:
                    dic_num[num_p] = contar
                
            except:
                # print({num_p:0})
                if contar != 0:
                    dic_num = dic_num | {num_p:contar}
            
        print(f'{int(_val)}|\n')
    frase = []
    for v,key in dic_num.items():
        if 1 < key:
            frase.append(f'{v}^{key}')
        else:
            frase.append(f'{v}')

    if len(frase) == 1:
        frase = frase[0]
    else:
        frase = ' · '.join(frase) + ' = ' + str(eval(' * '.join(frase).replace('^', '**')))
    print(f'El minmo cumun multiple es\n{frase}')
    # frase = ' · '.join(frase) + ' = ' + str(eval(' * '.join(frase).replace('^', '**')))
    # print(frase)

def maxim_comu_divisor(*valor):
    if len(valor) < 2:
        print('Inserte mas de dos valores separados por el caracter ","')
        return None
    all_dic = []
    for val in valor:
        _val = val
        print(f'Descomposicio factors del numero {val}')
        numeros_primos = numeros_primos_valor(val)[::-1][:-1]
        dic_num = {}
        for num_p in numeros_primos:
            contar = 0
            while True:
                if _val % num_p == 0:
                    print(f'{int(_val)}|{num_p}')
                    _val = _val / num_p
                    contar +=1
                else:
                    break
            try:
                if dic_num[num_p] < contar:
                    dic_num[num_p] = contar
                
            except:
                # print({num_p:0})
                if contar != 0:
                    dic_num = dic_num | {num_p:contar}
        all_dic.append(dic_num)    
        print(f'{int(_val)}|\n')

    # print(all_dic)
    new_val = []
    for dic in all_dic:
        for v,k in dic.items():
            new_val.append(v)
    # print(new_val)
    # print(list(set(new_val)))
    valor_rep = []
    for lnr in list(set(new_val)):
        contar = 0
        for nv in new_val:
            if lnr == nv:
                contar += 1
        if 1 < contar:
            valor_rep.append(lnr)

    # print(valor_rep)
    frase = []
    for key in valor_rep:
        i = 0
        for dic in all_dic:
            if i == 0:
                try:
                    v = dic[key]
                    i += 1
                except:
                    pass
            else:
                try:
                    if dic[key] < v:
                        v = dic[key]
                except:
                    pass

        if 1 < v:
            frase.append(f'{key}^{v}')
        else:
            frase.append(f'{key}')
    if len(frase) == 1:
        frase = frase[0]
    else:
        frase = ' · '.join(frase) + ' = ' + str(eval(' * '.join(frase).replace('^', '**')))
    print(f'El maximo cumun divisor es\n{frase}')

# def dividir(numerador,denominador):
#     coma = False
#     numerador_str = str(numerador)
#     denominador_len = len(str(denominador))
#     print(f'{numerador}|{denominador}_')
#     inici = 0
#     fin = denominador_len
#     resoltado = ''
#     while True:
#         while True:
#             if '.' in numerador_str[inici:fin]:
#                 if not coma:
#                     resoltado += '.'
#                 coma = True
#                 fin += 1
#             try:
#                 new_num = int(numerador_str[inici:fin].replace('.',''))
#             except:
#                 numerador_str += '0'
#                 if not coma:
#                     resoltado += '.'
#                 coma = True
#                 new_num = int(numerador_str[inici:fin].replace('.',''))
#             # print(new_num)
#             if new_num == 0:
#                 break
#             if new_num < denominador:
#                 fin += 1
#             else:
#                 break
#         i = 0
#         while True:
            
#             if new_num <= i*denominador:
#                 # residuo = new_num - i*denominador
#                 break
#             i += 1
#         if new_num != 0:
#             # print(new_num,i)
#             print(f'{new_num - (i)*denominador}|')
#         resoltado += str(i)

#         numerador_str = numerador_str.replace(numerador_str[inici:fin],'')
#         if numerador_str == '':
#             break
#     print(resoltado)
# dividir(numerador = 152,denominador = 5)
