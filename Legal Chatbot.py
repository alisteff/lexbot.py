import streamlit as st
import random

# Descripción del Consultorio Jurídico Civil
st.set_page_config(page_title="Consultorio Jurídico Civil", page_icon="⚖️")
st.title("⚖️ Consultorio Jurídico Civil")
st.write("Bienvenido al Consultorio Jurídico Civil. Este chatbot está diseñado para responder preguntas sobre temas legales en el área civil. Puedes consultar sobre arrendamientos, contratos, deudas y otros temas relacionados. Recuerda que esta información es general y siempre es recomendable acudir a un abogado para asesoría específica.")

def responder_pregunta(pregunta):
    respuestas = {
        "derechos como arrendatario": "Tienes derecho a un contrato escrito, a que no te suban el arriendo arbitrariamente y a la privacidad en tu vivienda.",
        "demandar por incumplimiento de contrato": "Debes presentar una demanda civil ante un juez con las pruebas del incumplimiento.",
        "me demandan por una deuda": "Debes responder a la demanda dentro del plazo legal y, si es necesario, contratar un abogado.",
        "tiempo para reclamar por daños en un contrato": "Depende del tipo de contrato, pero en general tienes hasta 5 años para reclamar.",
    }
    
    for clave in respuestas:
        if clave in pregunta.lower():
            return respuestas[clave]
    
    return "Lo siento, no tengo información sobre eso. Te recomiendo consultar con un abogado especializado en derecho civil."

pregunta = st.text_input("Escribe tu pregunta sobre derecho civil:")
if st.button("Consultar"):
    respuesta = responder_pregunta(pregunta)
    st.write("📝 Respuesta:", respuesta)
