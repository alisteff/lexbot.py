import streamlit as st
import random
import pyttsx3
import requests
from bs4 import BeautifulSoup
import threading
import re

# Configuración de la página
st.set_page_config(page_title="⚖️ Consultorio Jurídico Civil", page_icon="⚖️", layout="wide")

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

# Mostrar solo una vez el mensaje de bienvenida
if "bienvenida_reproducida" not in st.session_state:
    bienvenida = "Hola, soy LexBot, tu asistente legal. Estoy aquí para responder tus preguntas sobre derecho civil. ¿En qué puedo ayudarte hoy?"
    hablar(bienvenida)
    st.session_state["bienvenida_reproducida"] = True

# Agregar animación con CSS
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #e3f2fd, #bbdefb);
        font-family: Arial, sans-serif;
    }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    .robot {
        animation: bounce 2s infinite;
        display: block;
        margin: auto;
        width: 250px;
        filter: drop-shadow(0px 0px 10px rgba(0, 0, 0, 0.2));
    }
    .nav-button {
        background-color: #4A90E2;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        margin: 5px;
        transition: background-color 0.3s, transform 0.2s;
    }
    .nav-button:hover {
        background-color: #357ABD;
        transform: scale(1.05);
    }
    .titulo {
        text-align: center;
        color: #4A90E2;
        font-size: 30px;
        font-weight: bold;
    }
    .subtitulo {
        text-align: center;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Menú de navegación
menu = st.sidebar.radio("Navegación", ["Inicio", "Preguntas Frecuentes", "Consulta Legal", "Curiosidades"])

if menu == "Inicio":
    st.markdown("""
        <h1 class='titulo'>⚖️ Consultorio Jurídico Civil</h1>
        <p class='subtitulo'>Hola, soy <strong>LexBot</strong>, tu asistente legal virtual. Estoy aquí para responder preguntas sobre derecho civil, incluyendo arrendamientos, contratos y deudas. La información proporcionada es general; para asesoría específica, consulta con un abogado.</p>
        """, unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712068.png", caption="LexBot - Asistente Jurídico Virtual", use_container_width=True)

elif menu == "Preguntas Frecuentes":
    st.markdown("""
    ### 📌 Preguntas Frecuentes:
    - 🏠 **¿Cuáles son mis derechos como arrendatario?**
      - Tienes derecho a un contrato escrito, a que no te suban el arriendo arbitrariamente y a la privacidad en tu vivienda.
    - 📜 **¿Cómo puedo demandar por incumplimiento de contrato?**
      - Debes presentar una demanda civil ante un juez con las pruebas del incumplimiento.
    - ⚖️ **¿Qué hago si me demandan por una deuda?**
      - Debes responder a la demanda dentro del plazo legal y, si es necesario, contratar un abogado.
    - ⏳ **¿Cuánto tiempo tengo para reclamar por daños en un contrato?**
      - Depende del tipo de contrato, pero en general tienes hasta 5 años para reclamar.
    - 🏛️ **¿Qué ocurre si no pago una deuda?**
      - El acreedor puede iniciar un proceso judicial para exigir el pago.
    - 📝 **¿Es obligatorio registrar un contrato de arrendamiento?**
      - En algunos casos sí, especialmente para efectos fiscales y de seguridad jurídica.
    """, unsafe_allow_html=True)

elif menu == "Consulta Legal":
    st.markdown("<h3>📝 Escribe tu pregunta sobre derecho civil:</h3>", unsafe_allow_html=True)
    pregunta = st.text_input("Tu consulta aquí...")

    col1, col2 = st.columns([3, 1])
    with col1:
        usar_voz = st.checkbox("🗣️ Activar respuesta hablada")
    with col2:
        consulta = st.button("🔎 Consultar")

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
        
        return "🔍 No encontré una respuesta en la base de datos, intenta reformular tu pregunta."

    if consulta:
        respuesta = responder_pregunta(pregunta)
        st.markdown(f"<h4 style='color: #2E8B57;'>📝 Respuesta de LexBot:</h4> <p>{respuesta}</p>", unsafe_allow_html=True)
        
        if usar_voz:
            hablar(respuesta)
        
        st.image("https://source.unsplash.com/400x200/?law,justice", caption="Imagen relacionada", use_container_width=True)

elif menu == "Curiosidades":
    st.markdown("""
    ### 📚 Curiosidades sobre el Derecho Civil
    - ⚖️ **El derecho civil regula la mayoría de las interacciones diarias, desde contratos hasta herencias.**
    - 📜 **El Código Civil más antiguo aún en uso es el Código Napoleónico de 1804.**
    - 🏛️ **Las primeras leyes escritas se remontan al Código de Hammurabi en Babilonia.**
    """, unsafe_allow_html=True)
    st.image("https://source.unsplash.com/400x200/?law", caption="Curiosidades del derecho", use_container_width=True)
