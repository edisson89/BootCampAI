"""
src/generar_pdf.py - Este script CREA el archivo
"""

from reportlab.pdfgen import canvas

NOMBRE_ARCHIVO = "documento.pdf"


def crear_pdf():
    """
    Docstring para crear_pdf
    """
    print(f"🔨 Fabricando {NOMBRE_ARCHIVO}...")
    try:
        c = canvas.Canvas(NOMBRE_ARCHIVO)
        c.setFont("Helvetica", 20)
        c.drawString(100, 750, "¡Hola Bootcamp IA!")
        c.drawString(100, 700, "Este es un PDF de prueba generado con Python.")
        c.drawString(100, 650, "Aquí probamos la limpieza y el chunking.")
        c.drawString(100,650,'El mejor Programador es Edisson.')
        c.save()
        print(f"✅ ¡Éxito! Archivo '{NOMBRE_ARCHIVO}' creado en la carpeta raíz.")
    except Exception as e:
        print(f"❌ Error creando PDF: {e}")


if __name__ == "__main__":
    crear_pdf()
