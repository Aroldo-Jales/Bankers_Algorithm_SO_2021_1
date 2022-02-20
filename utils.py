import numpy as np

def vector_existing_resources(cols): # vetor de recursos existentes
    vector = np.zeros((cols), dtype=int)
    
    print('\nPreencha o vetor de recursos existentes.')
    
    for i in range(cols):
        try:
            value = int(input(f'Recurso {i+1} = '))
            vector[i] = value
        except ValueError:
            print('Valor inválido!')
            continue

    return vector

def matrix_alocation(rows, cols, t): # matriz de alocação corrente e requisição
    matrix = np.zeros((rows,cols), dtype=int)
    
    if t == 'C':
        print('\nPreencha a matriz de alocação corrente.')
    else:
        print('\nPreencha a matriz de requisições')

    for i in range(rows):
        for j in range(cols):
            try:
                value = int(input(f'Processo: {i+1} Recurso: {j+1} = ')) 
                matrix[i,j] = value
            except ValueError:
                print('Valor inválido!')
                continue

    return matrix

def vector_total_alocation(matrix): # vetor de recursos alocação corrente 

    cols = len(matrix[0])
    
    vector = np.zeros((cols), dtype=int)

    for i in range(cols):
        for values in matrix:
            vector[i] += values[i]

    return vector 

def vector_avaible_resources(vector1, vector2): # vetor de recursos disponíveis

    size = len(vector1)
    vector = np.zeros((size), dtype=int)
    
    for i in range(size):
        if vector1[i] >= vector2[i]:
            vector[i] = vector1[i] - vector2[i]
        else:
            vector = []
            return vector

    return vector

def is_lower_or_equal(vector1, vector2):
    count = 0
    for i in range(len(vector1)):
        if vector1[i] <= vector2[i]:
            count += 1
        else:
            return False

    if count == len(vector1):
        return True

def sum_vectors(vector1, vector2):
    vector = np.zeros(len(vector1), dtype=int)

    for i in range(len(vector1)):
        vector[i] = vector1[i] + vector2[i]
    return vector

def print_matrix(matrix, t):
    rows = len(matrix)

    if t == 'C':
        print('\nC = ')
    else:
        print('\nR = ')

    for i in range(rows):
        print(matrix[i])


def print_resources(resources, t):
    if t == 'E':
        print(f'\nE = {resources}')
    else:
        print(f'\nA = {resources}')
    
def print_all(current_allocation, avaible_resources, deadlock):
    if (deadlock):
        print('\nHouve Deadlock!''\n___________________________________________________\n')
    else:
        print('\nNão houve Deadlock!''\n___________________________________________________\n')
    
    print_matrix(current_allocation,'C')
    print_resources(avaible_resources, 'A')
    print('')
    
def queue_process(request_matrix, queue, current_allocation, avaible_resources, rows, cols):
    executed = []
    process_number = 0

    for i in range(len(queue)):
        current_process = request_matrix[queue[i]]
        current_process_alo = current_allocation[queue[i]]
        if is_lower_or_equal(current_process, avaible_resources):
            print(f'Processo {i+1} foi executado')
            print(f'P{i+1} = {current_process}')
            print(f'A = {avaible_resources} + C = {current_process_alo}')
            avaible_resources = sum_vectors(avaible_resources, current_process_alo)
            print(f'A = {avaible_resources}\n')
            executed.append(i)
            process_number = i
            for j in range(cols):
                request_matrix[queue[i]][j] = 0
                current_allocation[queue[i]][j] = 0
        else:
            print(f'Processo {queue[i]+1} não foi executado')
            print(f'P{i+1} = {current_process}\n')
    
    if len(executed) == 0:
        if len(queue) == 0:
            print_all(current_allocation, avaible_resources, deadlock=False)
        else:
            print_all(current_allocation, avaible_resources, deadlock=True)

    else:
        queue.remove(process_number)        
        queue_process(request_matrix, queue, current_allocation, avaible_resources, rows, cols)
            
def algorithm(request_matrix, current_allocation, avaible_resources, rows, cols): # algoritmo do banqueiro
    executed = []
    queue = []
    print('\nProcessos__________________________________________\n')

    for i in range(rows):
        current_process = request_matrix[i]
        current_process_alo = current_allocation[i]
        if is_lower_or_equal(current_process, avaible_resources):
            print(f'Processo {i+1} foi executado')
            print(f'P{i+1} = {current_process}')
            print(f'A = {avaible_resources} + C = {current_process_alo}')
            avaible_resources = sum_vectors(avaible_resources, current_process_alo)
            print(f'A = {avaible_resources}\n')
            executed.append(i)
            for j in range(cols):
                request_matrix[i][j] = 0       
                current_allocation[i][j] = 0 
        else:
            print(f'Processo {i+1} não foi executado')
            print(f'P{i+1} = {current_process}\n')
            queue.append(i)
    
    if len(queue) != 0:
        if len(executed) == 0:
            print_all(current_allocation, avaible_resources, deadlock=True)
        else:
            queue_process(request_matrix, queue, current_allocation, avaible_resources, rows, cols)
    else:
        print_all(current_allocation, avaible_resources, deadlock=False)