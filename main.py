"""
Script Completo: Ingesta -> Limpieza -> Chunking
Bootcamp IA - Semana 1
"""

import os
import re
from pypdf import PdfReader

# --- CONFIGURACIÓN ---
NOMBRE_PDF = "documento.pdf"
# ---------------------


def limpiar_texto(texto_crudo):
    """
    Fase 2: Limpieza
    Elimina saltos de línea y espacios extra.
    """
    texto = texto_crudo.replace("\n", " ")
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip()


def crear_chunks(texto, tamano=100):
    """
    Fase 3: Chunking (NUEVA FUNCIÓN)
    Corta el texto en pedazos de 'tamano' caracteres.
    """
    chunks = []
    # Recorremos el texto dando saltos de 'tamano' en 'tamano'
    for i in range(0, len(texto), tamano):
        trozo = texto[i : i + tamano]
        chunks.append(trozo)
    return chunks


def extraer_texto():
    print(f"📂 Carpeta actual: {os.getcwd()}")

    if not os.path.exists(NOMBRE_PDF):
        print(f"❌ ERROR: No encuentro '{NOMBRE_PDF}'.")
        print("   -> Asegúrate de que el archivo esté en esta misma carpeta.")
        return

    try:
        reader = PdfReader(NOMBRE_PDF)
        print(f"✅ PDF encontrado. Procesando {len(reader.pages)} páginas...\n")

        texto_completo = ""

        for i, pagina in enumerate(reader.pages):
            texto_sucio = pagina.extract_text()

            if texto_sucio:
                # 1. Limpiamos
                texto_limpio = limpiar_texto(texto_sucio)

                # 2. Creamos los CHUNKS (Pedacitos)
                mis_chunks = crear_chunks(texto_limpio, tamano=100)

                print(f"--- Página {i+1}: Se generaron {len(mis_chunks)} chunks ---")

                # Mostramos los primeros 3 chunks como ejemplo
                for k, chunk in enumerate(mis_chunks[:3]):
                    print(f"   [Chunk {k+1}]: {chunk}")
                print("   ...\n")

                texto_completo += texto_limpio + " "

        # Guardamos todo junto por si acaso
        with open("resultado.txt", "w", encoding="utf-8") as f:
            f.write(texto_completo)
        print("💾 Texto completo guardado en 'resultado.txt'.")

    except Exception as e:
        print(f"💥 Error: {e}")


if __name__ == "__main__":
    extraer_texto()
