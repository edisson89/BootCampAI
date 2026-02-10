from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Plan de Estudio Intensivo: AI Engineer (30 Dias)', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 5, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# Intro
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 5, "Objetivo: Convertirse en Ingeniero de IA Aplicada.\nEstrategia: 'Construir para Entender'.\nEnfoque: 50% Teoria / 50% Practica.\n\nHerramientas clave: Python, LangChain, FastAPI, OpenAI/HuggingFace.\n")
pdf.ln(5)

# Semana 1
pdf.chapter_title('Semana 1: Fundamentos de LLMs y Prompt Engineering')
pdf.chapter_body(
"""Objetivo: Entender como 'piensan' los modelos y controlarlos via API.

[50% Teoria]
- Arquitectura Transformer (tokens, contexto).
- Prompt Engineering avanzado (Few-shot, Chain of Thought).
- Parametros de inferencia (Temperature, Top-k).

[50% Practica]
- Dia 1-2: Llamadas a API de OpenAI con Python (sin librerias externas).
- Dia 3-5: Chatbot de consola con 'personalidad' (System Prompt).
- Dia 6-7: Generador de scripts para RRSS (output en JSON estructurado).
""")

# Semana 2
pdf.chapter_title('Semana 2: RAG (Retrieval-Augmented Generation)')
pdf.chapter_body(
"""Objetivo: Conectar la IA a tus propios datos (PDFs, Bases de datos).

[50% Teoria]
- Embeddings (Texto a vectores).
- Bases de Datos Vectoriales (ChromaDB, Pinecone).
- Busqueda Semantica vs. Keyword Search.

[50% Practica]
- Dia 8-10: Script que lea PDF, haga chunking y guarde en Vector DB.
- Dia 11-14: Crear un 'Chat con tu PDF'. El sistema busca fragmentos y responde basandose solo en el documento.
""")

# Semana 3
pdf.chapter_title('Semana 3: Agentes y Herramientas (LangChain)')
pdf.chapter_body(
"""Objetivo: Darle 'manos' a la IA para ejecutar acciones.

[50% Teoria]
- Concepto de Agentes y Tools.
- Razonamiento y Planificacion (ReAct).
- Function Calling.

[50% Practica]
- Dia 15-17: Agente que usa calculadora y busca en Google (Tavily/Serper).
- Dia 18-21: Asistente de Ventas conectado a SQL (Consultar stock/inventario).
""")

# Semana 4
pdf.chapter_title('Semana 4: Modelos Open Source y Despliegue')
pdf.chapter_body(
"""Objetivo: No depender solo de APIs cerradas y salir a produccion.

[50% Teoria]
- Modelos Open Source (Llama 3, Mistral).
- Quantization (correr en local).
- Intro a Fine-Tuning.

[50% Practica]
- Dia 22-25: Correr LLM local con Ollama/LM Studio y conectarlo a Python.
- Dia 26-30: PROYECTO FINAL.
  1. Backend: FastAPI.
  2. Logica: RAG o Agente.
  3. Frontend: Streamlit.
  4. Deploy: Railway/Render.
""")

# Rutina
pdf.chapter_title('Rutina Diaria (Regla 50/50)')
pdf.chapter_body(
"""- Hora 1-2 (Teoria): Ver curso/video y leer documentacion oficial. Entender el 'por que'.
- Hora 3-4 (Practica): Abrir VS Code. Romper el codigo. Cambiar prompts, bases de datos y modelos. Leer los errores.""")

# Guardar
pdf.output('Plan_Estudio_AI_30_Dias.pdf')
print("PDF generado exitosamente: 'Plan_Estudio_AI_30_Dias.pdf'")