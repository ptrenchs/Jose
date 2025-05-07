import random
import numpy as np
import pandas as pd
import ipywidgets as widgets
from datetime import datetime
from IPython.display import display
from IPython.display import clear_output

def sel_num(num_str):
    numeros = []
    for i in num_str:
        if i.isdigit():
            numeros.append(int(i))
    return numeros

def tablas(*numeros):
    if len(numeros) == 0:
        col = [i + 1 for i in range(10)]
        # fil = [i + 1 for i in range(10)]
    elif len(numeros) == 1:
        col = [numeros[0]]
    elif len(numeros) == 2:
        col = [i + 1 for i in range(numeros[0] - 1, numeros[1])]
    else:
        col = numeros
    matriz_respuestas = []
    matriz = []
    for i in col:
        # matriz.append([])
        matriz_respuestas.append([])
        for j in range(11):
            matriz.append(f'{i} x {j}')
            matriz_respuestas[-1].append('No eval')
    # print(matriz)
    try:
        while True:
            t_in = datetime.now()
            enunciado = random.choice(matriz)
            i = 0
            while True:
                if i == 0:
                    print(f'Completa la siguiente operacion {enunciado} es')
                    try:
                        resoltado = !read entrada; echo $entrada
                    except:
                        pass
                    clear_output()
                    try:
                        resoltado = resoltado[0]
                    except:
                        break
                    i += 1
                else:
                    clear_output()
                    print(f'Respuesta incorrecta {enunciado} es')
                    # resoltado = input()
                    try:
                        resoltado = !read entrada; echo $entrada
                    except:
                        pass
                    clear_output()
                    try:
                        resoltado = resoltado[0]
                    except:
                        break

                if float(resoltado) == float(eval(enunciado.replace('x', '*'))):
                    t_fin = datetime.now()
                    delta_t = t_fin - t_in
                    delta_t = round(delta_t.total_seconds(), 3)
                    all_num = sel_num(enunciado)
                    num_max = int(max(all_num) - 1)
                    num_min = int(min(all_num) - 1)
                    if matriz_respuestas[num_min][num_max] == 'No eval':
                        matriz_respuestas[num_min][num_max] = delta_t
                    else:
                        matriz_respuestas[num_min][num_max] = min(matriz_respuestas[num_min][num_max], delta_t)
                    # print(f'Respuesta correcta\nTiempo transcurrido: {delta_t}')
                    break
                del resoltado
            
            try:
                resoltado = resoltado[0]
            except:
                clear_output()
                break

            matriz.remove(enunciado)
            if matriz == []:
                break
            # time.sleep(3)
            clear_output()
        # print(col,resoltado)
        # print(dict(zip(col,matriz_respuestas)))
        display(pd.DataFrame(dict(zip(col,matriz_respuestas))))
    except KeyboardInterrupt:
        clear_output()
        # print('Programa detenido')
        display(pd.DataFrame(dict(zip(col,matriz_respuestas))))