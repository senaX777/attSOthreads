import multiprocessing
import random
import time

def soma(id, v):
    s = 0
    i =0
    while i < 5:
        s += v[i]
        i += 1
        time.sleep(0.2) 
    print(id, ',', s)

def main():
    id = 1
    v = [0]*5
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    n3 = random.randint(1, 100)
    n4 = random.randint(1, 100)
    n5 = random.randint(1, 100)
    v = [n1, n2, n3, n4, n5]
    parametros = [(0,0)]*3
    for i in range(0, 3, 1):
        parametros[i] = (id, v)
        id += 1
    with multiprocessing.Pool(processes=3) as threads:
        threads.starmap(soma, parametros)
if (__name__ == '__main__'):
    main()
