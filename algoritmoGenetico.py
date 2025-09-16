def gerar_individuo():
    return reparar([random.randint(0, 1) for _ in range(n)])

def populacao_inicial(size=50):
    return [gerar_individuo() for _ in range(size)]

def torneio(pop, k=3):
    competidores = random.sample(pop, k)
    return max(competidores, key=lambda ind: avaliar(ind)[0])

def crossover(pai1, pai2):
    if random.random() < 0.9:
        ponto = random.randint(1, n-1)
        filho1 = pai1[:ponto] + pai2[ponto:]
        filho2 = pai2[:ponto] + pai1[ponto:]
        return reparar(filho1), reparar(filho2)
    return pai1[:], pai2[:]

def mutacao(ind, p_mut=0.02):
    for i in range(n):
        if random.random() < p_mut:
            ind[i] = 1 - ind[i]
    return reparar(ind)

def algoritmo_genetico(pop_size=50, geracoes=120):
    populacao = populacao_inicial(pop_size)
    for _ in range(geracoes):
        nova_pop = []


        elite = sorted(populacao, key=lambda ind: avaliar(ind)[0], reverse=True)[:2]
        nova_pop.extend(elite)


        while len(nova_pop) < pop_size:
            pai1, pai2 = torneio(populacao), torneio(populacao)
            filho1, filho2 = crossover(pai1, pai2)
            filho1 = mutacao(filho1)
            filho2 = mutacao(filho2)
            nova_pop.extend([filho1, filho2])

        populacao = nova_pop[:pop_size]

    melhor = max(populacao, key=lambda ind: avaliar(ind)[0])
    melhor_valor, melhor_peso = avaliar(melhor)
    return melhor, melhor_valor, melhor_peso

melhor_solucao_AG, valor_final_AG, peso_final_AG = algoritmo_genetico()
print("Melhor solução encontrada (AG):", melhor_solucao_AG)
print("Valor total:", valor_final_AG)
print("Peso total:", peso_final_AG)
print("Itens escolhidos:", [i+1 for i in range(n) if melhor_solucao_AG[i] == 1])
