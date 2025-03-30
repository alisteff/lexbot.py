import streamlit as st
import random
import pyttsx3
import requests
from bs4 import BeautifulSoup
import threading
import re

# Configuración de la página
st.set_page_config(page_title="⚖️ Consultorio Jurídico Civil", page_icon="⚖️")

# Configuración del motor de voz
def init_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Ajustar si tienes una voz similar a Cortana
    return engine

def hablar(texto):
    def speak():
        engine = init_engine()
        texto_sin_emojis = re.sub(r'[^\w\s.,]', '', texto)  # Eliminar emojis
        engine.say(texto_sin_emojis)
        engine.runAndWait()
    threading.Thread(target=speak).start()

# Encabezado con estilo
st.markdown(
    """
    <h1 style='text-align: center; color: #4A90E2;'>⚖️ Consultorio Jurídico Civil</h1>
    <p style='text-align: center; font-size: 18px;'>Hola, soy <strong>LexBot</strong>, tu asistente legal virtual. Estoy aquí para responder preguntas sobre derecho civil, incluyendo arrendamientos, contratos y deudas. La información proporcionada es general; para asesoría específica, consulta con un abogado.</p>
    """, unsafe_allow_html=True
)

# Agregar animación con CSS
st.markdown(
    """
    <style>
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    .robot {
        animation: bounce 2s infinite;
        display: block;
        margin: auto;
        width: 250px;
    }
    </style>
    <img src="https://cdn-icons-png.flaticon.com/512/4712/4712068.png" class="robot">
    """,
    unsafe_allow_html=True
)

# Reproducir mensaje de bienvenida automáticamente
bienvenida = "Hola, soy LexBot, tu asistente legal. Estoy aquí para responder tus preguntas sobre derecho civil. ¿En qué puedo ayudarte hoy?"
hablar(bienvenida)

# Listado de preguntas frecuentes
st.markdown("""
### 📌 Preguntas Frecuentes:
- 🏠 ¿Cuáles son mis derechos como arrendatario?
- 📜 ¿Cómo puedo demandar por incumplimiento de contrato?
- ⚖️ ¿Qué hago si me demandan por una deuda?
- ⏳ ¿Cuánto tiempo tengo para reclamar por daños en un contrato?
""", unsafe_allow_html=True)

# Función para responder preguntas
def responder_pregunta(pregunta):
    respuestas = {
        "derechos como arrendatario": "🏠 Tienes derecho a un contrato escrito, a que no te suban el arriendo arbitrariamente y a la privacidad en tu vivienda.",
        "demandar por incumplimiento de contrato": "📜 Debes presentar una demanda civil ante un juez con las pruebas del incumplimiento.",
        "me demandan por una deuda": "⚖️ Debes responder a la demanda dentro del plazo legal y, si es necesario, contratar un abogado.",
        "tiempo para reclamar por daños en un contrato": "⏳ Depende del tipo de contrato, pero en general tienes hasta 5 años para reclamar.",
    }
    
    for clave in respuestas:
        if clave in pregunta.lower():
            return respuestas[clave]
    
    return buscar_en_google(pregunta)

# Función para buscar respuestas en Google
def buscar_en_google(consulta):
    url = f"https://www.google.com/search?q={consulta}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        snippets = soup.find_all("span", class_="hgKElc")
        if snippets:
            return snippets[0].text
        else:
            return "🔍 No encontré una respuesta en Google, intenta reformular tu pregunta."
    else:
        return "⚠️ Error al buscar en Google."

# Interfaz de usuario
st.markdown("<h3>📝 Escribe tu pregunta sobre derecho civil:</h3>", unsafe_allow_html=True)
pregunta = st.text_input("Tu consulta aquí...")

col1, col2 = st.columns([3, 1])
with col1:
    usar_voz = st.checkbox("🗣️ Activar respuesta hablada")
with col2:
    consulta = st.button("🔎 Consultar")

if consulta:
    respuesta = responder_pregunta(pregunta)
    st.markdown(f"<h4 style='color: #2E8B57;'>📝 Respuesta de LexBot:</h4> <p>{respuesta}</p>", unsafe_allow_html=True)
    
    if usar_voz:
        hablar(respuesta)
    
    st.image("https://source.unsplash.com/400x200/?law,justice", caption="Imagen relacionada", use_container_width=True)
