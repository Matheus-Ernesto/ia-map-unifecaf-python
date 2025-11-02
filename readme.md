# Rota Inteligente – Otimização de Entregas com IA

Um projeto em **Python** voltado ao **cálculo eficiente de rotas** para motoboys e entregadores.  
O sistema aplica **algoritmos de Inteligência Artificial**, como busca heurística e agrupamento, para sugerir os melhores caminhos e reduzir tempo e custos de entrega.

Desenvolvido como uma **biblioteca desktop**, o projeto pode ser facilmente integrado em **APIs ou aplicativos locais**, permitindo que empresas de delivery otimizem suas operações de forma prática e automatizada.

---

## Funcionalidades

- Cálculo da rota mais eficiente entre múltiplos pontos de entrega.  
- Agrupamento de entregas próximas utilizando algoritmos de clustering (ex.: K-Means).  
- Representação da cidade como grafo, com pesos baseados em distância ou tempo estimado.  
- Estrutura modular para uso como biblioteca ou aplicação independente.  
- Ferramentas auxiliares para instalação automática e limpeza de cache.

---

## Estrutura do Projeto

src/

├─ lib/

│ ├─ init.py

│ ├─ ai_map.py # Algoritmos de IA e grafos

├─ main/

│ ├─ main.py # Exemplo de execução e interface principal

├─ weights/

│ ├─ weight.py # Cálculo de pesos (distância/tempo)

├─ how_use.py # Exemplo de uso da biblioteca

├─ auto_installer.py # Instalação automática de dependências

├─ clean_caches # Ferramenta para limpeza de caches

├─ readme.md

└─ image_show.jpg # Imagem ilustrativa do projeto

---

## Tecnologias Utilizadas

- **Python 3.x**
- **Algoritmos de busca:** A*, BFS, DFS  
- **Clustering:** K-Means  
- **Estruturas de grafos:** NetworkX (ou implementação própria)

---

Ilustração


Sobre o Projeto

Este projeto faz parte do desafio “Rota Inteligente: Otimização de Entregas com Algoritmos de IA”, cujo objetivo é aplicar conceitos de Inteligência Artificial Clássica para resolver problemas reais de logística.
A solução utiliza técnicas de busca e agrupamento para otimizar entregas de forma escalável, contribuindo para redução de custos e aumento da eficiência operacional.

Autor

Matheus Ernesto dos Santos

Engenharia da Computação – UNIFECAF