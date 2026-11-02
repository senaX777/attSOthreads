import multiprocessing
import time

def processa(id):
    time.sleep(0.5)
    print('Thread', id)

def main():
    identificador: int = 0
    cont: int = 0
    parametros: int = [0]*5
    while cont < 5:
        identificador = cont + 1
        parametros[cont] = identificador
        cont += 1

    with multiprocessing.Pool(processes=5) as threads:
        threads.map(processa, parametros)

if (__name__ == '__main__'):
    main()