from collections import Counter

def monte_carlo(algoritmo, n_exec=100):
    resultados = []
    for _ in range(n_exec):
        sol, valor, peso = algoritmo()
        resultados.append((tuple(sol), valor, peso))


    valores = [r[1] for r in resultados]
    melhores = max(valores)
    media = sum(valores) / len(valores)


    solucoes = [r[0] for r in resultados]
    contagem = Counter(solucoes)
    distintas = len(contagem)
    mais_frequente = contagem.most_common(1)

    return {
        "media": media,
        "melhor": melhores,
        "distintas": distintas,
        "mais_frequente": mais_frequente
    }

print("=== Monte Carlo Hill Climbing ===")
mc_HC = monte_carlo(hill_climbing, 100)
print(mc_HC)

print("\n=== Monte Carlo Simulated Annealing ===")
mc_SA = monte_carlo(simulated_annealing, 100)
print(mc_SA)

print("\n=== Monte Carlo Algoritmo Genético ===")
mc_AG = monte_carlo(algoritmo_genetico, 100)
print(mc_AG)
