"""
Author: Aroldo-Jales
Date    Created: 06-02-2021
"""

from utils import *
import sys

def main():

    while True:

        try:
            print('-_-_-Algoritmo do Banqueiro-_-_-''\n1- Iniciar''\n2- Exemplo''\n0- Sair')
            option = int(input('\nOpção: '))

            if option == 0:
                break
                
            elif option == 1:
                process = int(input('Digite a quantidade de processos: '))
                resources = int(input('Digite a quantidade de recursos: '))
                existing_resources = vector_existing_resources(resources)         
                print_resources(existing_resources, 'E') 
                current_allocation = matrix_alocation(process, resources, 'C')
                print_matrix(current_allocation, 'C')
                
                total_alocation = vector_total_alocation(current_allocation)
                
                avaible_resources = vector_avaible_resources(existing_resources, total_alocation)
                print_resources(avaible_resources, 'A')

                if (len(avaible_resources) == 0):
                    print('\nOs recursos de alocação corrente são maiores que os recursos existentes!\n')
                    return main()
                else:
                    request_matrix = matrix_alocation(process, resources, 'R')
                    print_matrix(request_matrix,'R')
                    algorithm(request_matrix, current_allocation, avaible_resources, process, resources)

            elif option == 2:
                print('1- Deadlock''\n2- Sem Deadlock')
                option = int(input('\nOpção: '))
                process = 3
                resources = 4
                existing_resources = [4,2,3,1]
                print_resources(existing_resources, 'E') 
                current_allocation = [[0,0,1,0],[2,0,0,1],[0,1,2,0]]
                print_matrix(current_allocation,'C')
                total_alocation = vector_total_alocation(current_allocation)
                avaible_resources = vector_avaible_resources(existing_resources, total_alocation)
                print_resources(avaible_resources, 'A')
                request_matrix = [[2,0,0,1],[1,0,1,0],[2,1,0,0]]
                
                if option == 1:
                    request_matrix[2][3] = 1

                elif option == 2:
                    pass

                print_matrix(request_matrix,'R')
                algorithm(request_matrix, current_allocation, avaible_resources, process, resources)

        except ValueError:
            print('Valor inválido!')
            continue
        except:
            print('Erro (',sys.exc_info()[0],') ocorrido.')

main()