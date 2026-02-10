import os
from pypdf import PdfReader

# --- CONFIGURACIÓN ---
NOMBRE_PDF = "documento.pdf"  # <--- ASEGÚRATE DE QUE TU PDF SE LLAME ASÍ
# ---------------------

def extraer_texto():
    print(f"🔍 Buscando archivo: {NOMBRE_PDF}...")
    
    if not os.path.exists(NOMBRE_PDF):
        print(f"❌ ERROR: No encuentro el archivo '{NOMBRE_PDF}' en esta carpeta.")
        print("   -> Solución: Pega un PDF aquí y cámbiale el nombre a 'documento.pdf'")
        return

    try:
        reader = PdfReader(NOMBRE_PDF)
        print(f"✅ PDF encontrado. Tiene {len(reader.pages)} páginas.\n")
        
        texto_completo = ""
        for i, pagina in enumerate(reader.pages):
            texto = pagina.extract_text()
            print(f"--- Página {i+1} ---")
            print(texto[:200] + "...\n") # Muestra solo los primeros 200 caracteres
            texto_completo += texto

        # Guardar en un txt para revisar luego
        with open("resultado.txt", "w", encoding="utf-8") as f:
            f.write(texto_completo)
        print("💾 Texto completo guardado en 'resultado.txt'")

    except Exception as e:
        print(f"💥 Error crítico: {e}")

if __name__ == "__main__":
    extraer_texto()