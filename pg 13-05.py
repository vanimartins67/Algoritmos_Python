import time
def pg (a1, q, n):
    result = a1
    print(result)
    inicio = time.time_ns
    for i in range (1, n+1):
        result = result * q
        print(result)
    fim = time.time_ns
    tempo = fim - inicio
    print("Tempo de execução: ", tempo)
    return result

a1 = 1

def pg(a1, q, n):
    result = a1 * q**(n-1)
    return result

def soma_pg_infinita (a1, q, n):
    return (a1 * (1-q**n) / (1-q))

def soma_pg_finita(a1, q, n):
    return (a1 * (1-q**n) / (1-q))

def produto_pg(a1, q, n):
    return ((a1**(n))*q**(n*(n-1) / 2))