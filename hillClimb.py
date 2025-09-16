import random

valores = [60, 100, 120, 90, 30, 70, 40, 160, 20, 50, 110, 85, 95, 200, 55]
pesos =  [10, 20, 30, 15, 5, 12, 7, 25, 3, 9, 18, 14, 16, 28, 6]
capacidade = 50
n = len(valores)

def avaliar(solucao):
    valor_total = sum(valores[i] for i in range(n) if solucao[i] == 1)
    peso_total = sum(pesos[i] for i in range(n) if solucao[i] == 1)
    return valor_total, peso_total

def reparar(solucao):
    while True:
        valor, peso = avaliar(solucao)
        if peso <= capacidade:
            return solucao

        idx = random.choice([i for i in range(n) if solucao[i] == 1])
        solucao[idx] = 0


def solucao_inicial():
    sol = [random.randint(0, 1) for _ in range(n)]
    return reparar(sol)


def gerar_vizinhos(solucao):
    vizinhos = []
    for i in range(n):
        vizinho = solucao[:]
        vizinho[i] = 1 - vizinho[i]
        vizinhos.append(reparar(vizinho))
    return vizinhos


def hill_climbing(max_iter=300):
    solucao = solucao_inicial()
    melhor_valor, melhor_peso = avaliar(solucao)

    for _ in range(max_iter):
        vizinhos = gerar_vizinhos(solucao)
        melhor_vizinho = max(vizinhos, key=lambda s: avaliar(s)[0])
        valor_vizinho, peso_vizinho = avaliar(melhor_vizinho)

        if valor_vizinho > melhor_valor and peso_vizinho <= capacidade:
            solucao = melhor_vizinho
            melhor_valor, melhor_peso = valor_vizinho, peso_vizinho
        else:
            break

    return solucao, melhor_valor, melhor_peso


melhor_solucao, valor_final, peso_final = hill_climbing()
print("Melhor solução encontrada (HC):", melhor_solucao)
print("Valor total:", valor_final)
print("Peso total:", peso_final)
print("Itens escolhidos:", [i+1 for i in range(n) if melhor_solucao[i] == 1])
