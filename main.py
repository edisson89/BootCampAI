"""
Pipeline ETL + Embeddings (Vectorización)
Bootcamp IA - Semana 1
"""
import os
import re
import json
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer  # <--- EL CEREBRO DE LA IA

NOMBRE_PDF = "documento.pdf"

# --- CARGAMOS EL MODELO DE IA (Se descarga la primera vez) ---
print("⏳ Cargando modelo de IA (esto puede tardar la primera vez)...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("✅ Modelo cargado y listo para pensar.")
# -------------------------------------------------------------

def limpiar_texto(texto):
    texto = texto.replace("\n", " ")
    return re.sub(r'\s+', ' ', texto).strip()

def crear_chunks(texto, tamano=100):
    chunks = []
    for i in range(0, len(texto), tamano):
        chunks.append(texto[i : i + tamano])
    return chunks

def procesar_pdf():
    if not os.path.exists(NOMBRE_PDF):
        print(f"❌ Error: No encuentro {NOMBRE_PDF}")
        return

    reader = PdfReader(NOMBRE_PDF)
    base_conocimiento = []

    print(f"🚀 Procesando {NOMBRE_PDF}...")

    for i, pagina in enumerate(reader.pages):
        texto = pagina.extract_text()
        if texto:
            chunks = crear_chunks(limpiar_texto(texto), tamano=150)

            for chunk in chunks:
                # 1. GENERAMOS EL VECTOR (EMBEDDING)
                # Esto convierte el texto en una lista de 384 números
                vector = model.encode(chunk).tolist()

                # 2. Guardamos todo junto
                dato = {
                    "id": len(base_conocimiento) + 1,
                    "texto": chunk,
                    "vector": vector,
                    "metadata": {
                        "fuente": NOMBRE_PDF,
                        "pagina": i + 1
                    }
                }
                base_conocimiento.append(dato)

    # Guardar JSON
    with open("base_conocimiento_vectorizada.json", "w", encoding="utf-8") as f:
        json.dump(base_conocimiento, f, indent=4)
    
    print(f"💾 ¡Listo! Revisa 'base_conocimiento_vectorizada.json'.")
    print(f"   -> Ahora cada chunk tiene su 'ADN' matemático.")

if __name__ == "__main__":
    procesar_pdf()