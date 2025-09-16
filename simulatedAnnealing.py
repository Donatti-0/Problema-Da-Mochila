import math

def simulated_annealing(T0=50.0, Tmin=0.1, alpha=0.95, passos_por_T=30):
    solucao = solucao_inicial()
    melhor_solucao = solucao[:]
    melhor_valor, melhor_peso = avaliar(solucao)

    T = T0

    while T > Tmin:
        for _ in range(passos_por_T):

            vizinho = gerar_vizinhos(solucao)
            candidato = random.choice(vizinho)
            valor_cand, peso_cand = avaliar(candidato)
            valor_atual, peso_atual = avaliar(solucao)


            delta = valor_cand - valor_atual

            if delta > 0 or random.random() < math.exp(delta / T):
                solucao = candidato[:]
                if valor_cand > melhor_valor and peso_cand <= capacidade:
                    melhor_solucao = candidato[:]
                    melhor_valor, melhor_peso = valor_cand, peso_cand
        T *= alpha

    return melhor_solucao, melhor_valor, melhor_peso

melhor_solucao_SA, valor_final_SA, peso_final_SA = simulated_annealing()
print("Melhor solução encontrada (SA):", melhor_solucao_SA)
print("Valor total:", valor_final_SA)
print("Peso total:", peso_final_SA)
print("Itens escolhidos:", [i+1 for i in range(n) if melhor_solucao_SA[i] == 1])
