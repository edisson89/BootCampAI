"""
Pipeline ETL con Metadatos y Exportación JSON
Bootcamp IA - Semana 1
"""
import os
import re
import json  # <--- Nuevo amigo: Para guardar datos estructurados
from pypdf import PdfReader

NOMBRE_PDF = "documento.pdf"

def limpiar_texto(texto):
    texto = texto.replace("\n", " ")
    return re.sub(r'\s+', ' ', texto).strip()

def crear_chunks(texto, tamano=150):
    chunks = []
    for i in range(0, len(texto), tamano):
        chunks.append(texto[i : i + tamano])
    return chunks

def procesar_pdf():
    if not os.path.exists(NOMBRE_PDF):
        print(f"❌ Primero genera el PDF con: python src/generar_pdf.py")
        return

    reader = PdfReader(NOMBRE_PDF)
    base_conocimiento = []  # Aquí guardaremos todo ordenado

    print(f"✅ Procesando {NOMBRE_PDF}...")

    for i, pagina in enumerate(reader.pages):
        texto_crudo = pagina.extract_text()
        
        if texto_crudo:
            texto_limpio = limpiar_texto(texto_crudo)
            lista_chunks = crear_chunks(texto_limpio, tamano=150)

            # --- LA MAGIA: Guardamos con METADATOS ---
            for chunk in lista_chunks:
                dato = {
                    "id": len(base_conocimiento) + 1,
                    "texto": chunk,
                    "metadata": {
                        "fuente": NOMBRE_PDF,
                        "pagina": i + 1,  # Guardamos el número de página real
                        "longitud": len(chunk)
                    }
                }
                base_conocimiento.append(dato)
            # -----------------------------------------

    # Guardar en JSON (Simulando una Base de Datos)
    with open("base_conocimiento.json", "w", encoding="utf-8") as f:
        json.dump(base_conocimiento, f, indent=4, ensure_ascii=False)
    
    print(f"💾 ¡Listo! Se guardaron {len(base_conocimiento)} chunks en 'base_conocimiento.json'")
    print("   -> Abre ese archivo para ver cómo quedó tu data estructurada.")

if __name__ == "__main__":
    procesar_pdf()