import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.ai_map_osm import RouteAI_OSM

def main():
    ai = RouteAI_OSM("São Paulo, Brazil")

    # Lista de pontos (lat, lon)
    pontos = [
        (-23.609903123319242, -46.768615411386975),  # Unifecaf Taboão
        (-23.59930295301864, -46.71912465622006),    # Estadio Morumbi
        (-23.562091773212586, -46.65563820973811),   # MASP
    ]

    rota_total = []
    dist_total = 0.0

    print(f"[→] Calculando rota para {len(pontos)} pontos ...")

    for i in range(len(pontos) - 1):
        origem = pontos[i]
        destino = pontos[i + 1]
        rota, dist = ai.find_route(origem, destino, algorithm="astar")

        # Adiciona rota (evita repetir o último nó)
        if rota_total:
            rota_total.extend(rota[1:])
        else:
            rota_total.extend(rota)

        dist_total += dist
        print(f" Trecho {i+1}: {round(dist/1000, 2)} km")

    print(f"\nDistância total: {round(dist_total/1000, 2)} km")
    print(f"Número total de nós: {len(rota_total)}")

    # Desenhar o mapa com a rota completa
    ai.plot_route(rota_total)

if __name__ == "__main__":
    main()
