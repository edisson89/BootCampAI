"""
Este script se encarga de extraer texto de archivos PDF.
Es parte del Bootcamp de IA - Semana 1.
"""

from reportlab.pdfgen import canvas

NOMBRE_ARCHIVO = "documento.pdf"


def crear_pdf_prueba():
    print(f"🔨 Creando archivo '{NOMBRE_ARCHIVO}'...")

    try:
        # Inicializar el lienzo (canvas)
        c = canvas.Canvas(NOMBRE_ARCHIVO)

        # Escribir texto en el PDF (Coordenadas X, Y)
        # Y=800 es arriba, Y=0 es abajo
        c.setFont("Helvetica", 20)
        c.drawString(100, 750, "¡Hola Mundo! Este es mi PDF de prueba.")

        c.setFont("Helvetica", 12)
        c.drawString(
            100, 720, "Este documento fue generado automáticamente con Python."
        )
        c.drawString(100, 700, "Estamos simulando datos para el Bootcamp de IA.")
        c.drawString(
            100, 680, "Línea 4: Datos de prueba para ingesta."
        )  # Guardar el archivo
        c.save()
        print(f"✅ ¡Listo! Archivo '{NOMBRE_ARCHIVO}' creado correctamente.")

    except Exception as e:
        print(f"❌ Error creando el PDF: {e}")


if __name__ == "__main__":
    crear_pdf_prueba()
