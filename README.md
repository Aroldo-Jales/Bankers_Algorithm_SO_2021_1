# Bankers_algorithm

https://www.wikitechy.com/technology/bankers-algorithm/

Algoritmo baseado numa matriz para detecção de deadlock com n processos 
e m classes de recursos diferentes.

#### Algoritmo:

1 . Procure por um processo desmarcado Pi, para o qual a enésima linha de R é menor do que a correspondente de A.

2. Se um processo com tais característica for encontrado, adicione a enésima linha de C a A, marque o processo e volte para o 
passo 1.

3. Se não houver nenhum processo nesta situação, o algoritmo termina.
  
```python

Exemplo:

  Recursos existentes:
    E = (4 2 3 1) 4 (dvdrw) 2 (plotters) 3 (impressoras) 1 (blue-ray)

  Recursos disponíveis: A = (2 1 0 0)

  Matriz de alocação corrente:
    C =
    0 0 1 0 P1
    2 0 0 1 P2
    0 1 2 0 P3

  Matriz de requisições:
    R =
    2 0 0 1 P1
    1 0 1 0 P2
    2 1 0 0 P3

  P3 (rodar) A = (2 2 2 0)
  P2 (rodar) A = (4 2 2 1)
  P1 (rodar) não há deadlock
  
  # Obs: Se R[3,4] fosse igual a 1, todo o processo estaria em deadlock.
  
```
