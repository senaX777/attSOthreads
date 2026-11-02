
import multiprocessing
import random
import time

def sapo(id, dist):
    p = 0
    while p < dist:
        salto = random.randint(1, 5)
        p = p + salto
        print('o sapo ', id, 'pulou', salto, 'CMs')
        time.sleep (0.3)
    print('Sapo', id, 'chegou')

def main():
    id: int = 1
    tam: int = 10
    parametros = [0]*5
    for i in range(0, 5, 1):
        parametros[i] = (id, tam)
        id += 1
    with multiprocessing.Pool(processes=5) as threads:
        threads.starmap(sapo, parametros)
if __name__ == '__main__':
    main()
