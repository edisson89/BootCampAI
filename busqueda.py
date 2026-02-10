"""
Motor de Búsqueda Semántica (RAG)
Compara la pregunta del usuario con los vectores guardados.
"""

import json
import numpy as np
from sentence_transformers import SentenceTransformer, util

# 1. Cargar la Base de Conocimiento
ARCHIVO_DB = "base_conocimiento_vectorizada.json"

print("⏳ Cargando cerebro (Modelo IA)...")
model = SentenceTransformer("all-MiniLM-L6-v2")


def buscar(pregunta, top_k=1):
    print(f"\n🔍 Analizando pregunta: '{pregunta}'...")

    # A. Convertir la PREGUNTA del usuario en vector
    vector_pregunta = model.encode(pregunta)

    # B. Cargar los datos
    with open(ARCHIVO_DB, "r", encoding="utf-8") as f:
        datos = json.load(f)

    # C. Comparar matemáticas (Similitud del Coseno)
    mejores_resultados = []

    for chunk in datos:
        # Recuperamos el vector del chunk (que guardamos antes)
        vector_chunk = np.array(chunk["vector"], dtype=np.float32)

        # Calculamos similitud (0 a 1)
        similitud = util.cos_sim(vector_pregunta, vector_chunk).item()

        # Guardamos el resultado
        mejores_resultados.append(
            {
                "texto": chunk["texto"],
                "score": similitud,
                "pagina": chunk["metadata"]["pagina"],
            }
        )

    # D. Ordenar por el que tenga mayor score (El más parecido)
    mejores_resultados.sort(key=lambda x: x["score"], reverse=True)

    return mejores_resultados[:top_k]


if __name__ == "__main__":
    # --- PRUEBA INTERACTIVA ---
    while True:
        usuario = input("\nPregunta algo al PDF (o escribe 'salir'): ")
        if usuario.lower() == "salir":
            break

        respuestas = buscar(usuario)

        if respuestas:
            ganador = respuestas[0]
            print(f"✅ Mejor coincidencia encontrada (Score: {ganador['score']:.4f}):")
            print(f"📖 Página {ganador['pagina']}:")
            print(f"📝 '{ganador['texto']}'")
        else:
            print("❌ No encontré nada relevante.")
