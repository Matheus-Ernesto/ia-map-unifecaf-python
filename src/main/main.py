# src/main/main.py
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.ai_map_osm import RouteAI_OSM

def main():
    ai = RouteAI_OSM("São Paulo, Brazil")

    # Coordenadas aproximadas
    origem = (-23.649, -46.852)   # Embu das Artes
    destino = (-23.559, -46.658)  # Av. Paulista

    rota, dist = ai.find_route(origem, destino, algorithm="astar")

    print(f"Distância total: {round(dist/1000, 2)} km")
    print(f"Número de nós: {len(rota)}")

    # Desenhar o mapa (opcional)
    ai.plot_route(rota)

if __name__ == "__main__":
    main()
    