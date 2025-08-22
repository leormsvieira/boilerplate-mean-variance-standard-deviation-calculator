import numpy as np

def calculate(list):
    # Verifica se a lista contém exatamente 9 elementos
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Converte a lista em uma matriz NumPy 3x3
    matrix = np.array(list).reshape(3, 3)

    # Calcula estatísticas para cada eixo
    # axis=0: colunas, axis=1: linhas, axis=None: matriz achatada

    # Média
    mean_axis0 = matrix.mean(axis=0).tolist()  
    mean_axis1 = matrix.mean(axis=1).tolist()  
    mean_flattened = matrix.mean().item()      

    # Variância
    var_axis0 = matrix.var(axis=0).tolist()    
    var_axis1 = matrix.var(axis=1).tolist()    
    var_flattened = matrix.var().item()       

    # Desvio padrão
    std_axis0 = matrix.std(axis=0).tolist()    
    std_axis1 = matrix.std(axis=1).tolist()    
    std_flattened = matrix.std().item()       

    # Máximo
    max_axis0 = matrix.max(axis=0).tolist()    
    max_axis1 = matrix.max(axis=1).tolist()    
    max_flattened = matrix.max().item()        

    # Mínimo
    min_axis0 = matrix.min(axis=0).tolist()    
    min_axis1 = matrix.min(axis=1).tolist()    
    min_flattened = matrix.min().item()        

    # Soma
    sum_axis0 = matrix.sum(axis=0).tolist()    
    sum_axis1 = matrix.sum(axis=1).tolist()    
    sum_flattened = matrix.sum().item()        

    # Cria o dicionário de retorno
    calculations = {
        'mean': [mean_axis0, mean_axis1, mean_flattened],
        'variance': [var_axis0, var_axis1, var_flattened],
        'standard deviation': [std_axis0, std_axis1, std_flattened],
        'max': [max_axis0, max_axis1, max_flattened],
        'min': [min_axis0, min_axis1, min_flattened],
        'sum': [sum_axis0, sum_axis1, sum_flattened]
    }

    return calculations