import streamlit as st
import pyttsx3
import threading
import time

# Configuración de la página
st.set_page_config(page_title="⚖️ Consultorio Jurídico - área civil", page_icon="⚖️", layout="wide")

# Configuración del motor de voz
def init_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    return engine

def hablar(texto):
    def speak():
        engine = init_engine()
        engine.say(texto)
        engine.runAndWait()
    threading.Thread(target=speak).start()

# Animación de carga
def animacion_carga():
    mensaje = "Procesando consulta."
    for _ in range(3):
        mensaje += " ."
        with st.empty():
            st.info(mensaje)
            time.sleep(0.5)

# Mostrar solo una vez el mensaje de bienvenida
if "bienvenida_reproducida" not in st.session_state:
    bienvenida = "Hola, soy Cortana, tu asistente legal especializado en Colombia. ¿En qué puedo ayudarte hoy?"
    hablar(bienvenida)
    st.session_state["bienvenida_reproducida"] = True

# Respuestas Predefinidas
respuestas_frecuentes = {
    "arrendatario": "Como arrendatario en Colombia, tienes derecho a un contrato escrito, a que no te suban el arriendo arbitrariamente y a tener privacidad en tu vivienda.",
    "incumplimiento_contrato": "Para demandar por incumplimiento de contrato en Colombia, debes presentar una demanda civil ante un juez y aportar pruebas del incumplimiento.",
    "deuda": "Si te demandan por una deuda, debes responder a la demanda dentro del plazo legal. Es recomendable contratar un abogado si es necesario."
}

# Función para manejar respuestas predefinidas
def obtener_respuesta(pregunta):
    if "arrendatario" in pregunta.lower():
        return respuestas_frecuentes["arrendatario"]
    elif "incumplimiento de contrato" in pregunta.lower():
        return respuestas_frecuentes["incumplimiento_contrato"]
    elif "deuda" in pregunta.lower():
        return respuestas_frecuentes["deuda"]
    else:
        return "Lo siento, no tengo una respuesta predefinida para esa consulta."

# Menú de navegación
menu = st.sidebar.radio("Navegación", ["Inicio", "Preguntas Frecuentes", "Consulta Legal", "Curiosidades", "Normativa Colombiana"])

if menu == "Inicio":
    st.markdown(""" 
        <h1 style='text-align: center; color: #8B4513;'>⚖️ Consultorio Jurídico - área civil ⚖️</h1>
        <p style='text-align: center;'>Soy <strong>Cortana</strong>, tu asistente legal virtual especializado en el derecho colombiano. Pregunta lo que necesites sobre contratos, arrendamientos, deudas y más.</p>
        """, unsafe_allow_html=True)
    # Imagen del inicio (puedes reemplazar 'static-image-1.png' con el nombre de tu imagen)
    st.image("static-image-1.png", caption="Cortana - Asistente Jurídico Virtual", use_container_width=True)

elif menu == "Preguntas Frecuentes":
    st.markdown("""
    ### 📌 Preguntas Frecuentes:
    
    **🏠 ¿Cuáles son mis derechos como arrendatario?**
    - ✅ Tienes derecho a un contrato escrito.
    - ✅ No pueden subir el arriendo arbitrariamente.
    - ✅ Debes tener privacidad en tu vivienda.
    
    **📜 ¿Cómo puedo demandar por incumplimiento de contrato?**
    - 📌 Debes presentar una demanda civil ante un juez.
    - 📌 Asegúrate de contar con pruebas del incumplimiento.
    
    **⚖️ ¿Qué hago si me demandan por una deuda?**
    - 🕐 Debes responder a la demanda dentro del plazo legal.
    - 👨‍⚖️ Si es necesario, contrata un abogado.
    """, unsafe_allow_html=True)

    # Aquí colocamos las imágenes 2 y 3 de forma alineada (una al lado de la otra)
    col1, col2 = st.columns(2)
    with col1:
        st.image("animated-image-2.gif", caption="Justicia y derecho", use_container_width=True)
    with col2:
        st.image("animated-image-3.gif", caption="Proceso Legal", use_container_width=True)

elif menu == "Consulta Legal":
    st.markdown("<h3>📝 Escribe tu pregunta sobre consultorio jurídico:</h3>", unsafe_allow_html=True)
    pregunta = st.text_input("Tu consulta aquí...")

    col1, col2 = st.columns([3, 1])
    with col1:
        usar_voz = st.checkbox("🗣️ Activar respuesta hablada")
    with col2:
        consulta = st.button("🔎 Consultar")

    if consulta:
        with st.spinner("Analizando tu consulta..."):
            animacion_carga()
            respuesta = obtener_respuesta(pregunta)
        
        st.markdown(f"<h4 style='color: #2E8B57;'>📝 Respuesta de LexBot:</h4> <p>{respuesta}</p>", unsafe_allow_html=True)
        
        if usar_voz:
            hablar(respuesta)

elif menu == "Normativa Colombiana":
    st.markdown("""
    ### 📜 Normativa Colombiana Relevante
    - **📕 Código Civil Colombiano:** Regula los derechos y obligaciones de las personas en sus relaciones civiles y comerciales.
    - **📘 Código Penal:** Establece las conductas consideradas delitos y sus respectivas sanciones.
    - **📗 Ley de Arrendamiento Urbano (Ley 820 de 2003):** Regula los contratos de arrendamiento de vivienda en Colombia.
    - **📙 Código General del Proceso:** Define los procedimientos judiciales en materia civil, comercial y de familia.
    """, unsafe_allow_html=True)

    # Aquí colocamos las imágenes 4 y 5 de forma alineada (una al lado de la otra)
    col1, col2 = st.columns(2)
    with col1:
        st.image("animated-image-4.gif", caption="Leyes de Colombia", use_container_width=True)
    with col2:
        st.image("animated-image-5.gif", caption="Constitución Colombiana", use_container_width=True)

elif menu == "Curiosidades":
    st.markdown("""
    ### 📚 10 Curiosidades sobre el Derecho en Colombia
    
    - El Código Civil Colombiano fue escrito por Andrés Bello y es base del derecho en varios países.
    - La Corte Constitucional ha protegido derechos fundamentales con sentencias clave.
    - Colombia reconoce el derecho al Habeas Data, garantizando acceso a información personal.
    - La Ley 1448 de 2011 garantiza reparación a víctimas del conflicto.
    - El primer Código Penal colombiano data de 1837.
    - La acción de tutela es una de las herramientas más utilizadas para proteger derechos.
    - En Colombia, los jueces pueden interpretar la ley bajo el principio de equidad.
    - La Constitución de 1991 fortaleció los mecanismos de participación ciudadana.
    - Existen juzgados especializados en temas ambientales.
    - La Defensoría del Pueblo vela por los derechos humanos.
    """, unsafe_allow_html=True)

    # Aquí colocamos las imágenes 6 y 7 de forma alineada (una al lado de la otra)
    col1, col2 = st.columns(2)
    with col1:
        st.image("animated-image-6.gif", caption="Curiosidades sobre el derecho", use_container_width=True)
    with col2:
        st.image("animated-image-7.gif", caption="Más curiosidades", use_container_width=True)

