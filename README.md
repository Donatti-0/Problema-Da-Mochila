# Reflexão Final

## O Hill Climbing travou em soluções locais?
**Sim.** Ele frequentemente ficou preso em soluções locais, pelo fato de só aceitar melhorias imediatas. Isso limita sua capacidade de explorar outras regiões do espaço de busca.

## O Simulated Annealing conseguiu escapar de ótimos locais?
**Sim.** Ele conseguiu escapar de ótimos locais em várias execuções, graças à aceitação de soluções piores no início, que foi reduzida conforme a temperatura caía.

## O Algoritmo Genético trouxe diversidade e soluções mais próximas do ótimo?
**Sim.** Ele manteve diversidade ao longo das gerações e apresentou maior valor, ficando mais próximo do ótimo global.

## Qual método foi mais rápido? E qual foi mais eficaz?
- **Mais rápido:** Hill Climbing, pois realiza uma busca simples e converge mais rapidamente.
- **Mais eficaz:** Algoritmo Genético, pois produziu as melhores soluções finais entre as execuções.

## Os três algoritmos são estocásticos. O que isso significa?
Ser **estocástico** significa que os algoritmos tomam decisões com base em aleatoriedade. Cada execução pode gerar resultados diferentes, mesmo com os mesmos parâmetros.  
Em contraste, algoritmos **não estocásticos** sempre geram o mesmo resultado para a mesma entrada, sem variação.

---

# Resultados Obtidos

## 1. Hill Climb
- **Média do valor encontrado:** 318.9  
- **Melhor valor obtido:** 350  
- **Número de soluções distintas:** 51  
- **Soluções mais frequentes:**  
  `[((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1), 10)]`

## 2. Simulated Annealing
- **Média do valor encontrado:** 349.85  
- **Melhor valor obtido:** 350  
- **Número de soluções distintas:** 3  
- **Soluções mais frequentes:**  
  `[((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1), 99)]`

## 3. Algoritmo Genético
- **Média do valor encontrado:** 350  
- **Melhor valor obtido:** 350  
- **Número de soluções distintas:** 1  
- **Soluções mais frequentes:**  
  `[((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1), 100)]`

---

# Comparações dos Algoritmos

## Qual método obteve o melhor resultado global?
**Algoritmo Genético**: apresentou a maior média de valor encontrado.

## Qual foi o mais consistente?
**Algoritmo Genético**: apresentou o menor número de soluções distintas.

## Qual apresentou maior diversidade de soluções?
**Hill Climb**: apresentou o maior número de soluções distintas.
