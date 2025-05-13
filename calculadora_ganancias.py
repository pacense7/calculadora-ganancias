import streamlit as st
import json
import urllib.parse

# Función para cargar animación Lottie (si la tienes más adelante)
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Estilos personalizados con CSS
def estilo_css():
    st.markdown("""
        <style>
            body {
                background-color: #f1f3f6;
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
            }
            .card {
                background-color: white;
                border-radius: 15px;
                padding: 20px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }
            .whatsapp-button {
                background-color: #D0E8D4;  /* Color más claro */
                color: #333;  /* Letras negras para mejor contraste */
                padding: 12px 24px;
                border-radius: 25px;
                text-decoration: none;
                font-size: 16px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                transition: background-color 0.3s;
                display: inline-block;
                margin-top: 20px;
            }
            .whatsapp-button:hover {
                background-color: #A3D0A1;  /* Color más oscuro al hacer hover */
            }
            .slider .stSlider {
                border-radius: 20px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }
            .stSlider .track {
                background-color: #00a082;
            }
            .info-button {
                background-color: transparent;
                border: none;
                color: #00a082;
                cursor: pointer;
                font-size: 18px;
                font-weight: bold;
            }
            .info-text {
                display: none;
                padding: 15px;
                background-color: #f1f1f1;
                border-radius: 8px;
                margin-top: 10px;
                font-size: 14px;
                color: #333;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }
            .info-text.show {
                display: block;
            }
            .header {
                text-align: center;
                color: #00a082;
                font-size: 2.5rem;
                font-weight: bold;
            }
            .footer {
                text-align: center;
                margin-top: 40px;
            }
            /* Estilos responsivos */
            @media (max-width: 600px) {
                .header {
                    font-size: 2rem;
                }
                .whatsapp-button {
                    font-size: 14px;
                    padding: 10px 20px;
                }
                .card {
                    padding: 15px;
                }
            }
        </style>
    """, unsafe_allow_html=True)

estilo_css()

# Título
st.markdown("""
    <div class='card'>
        <h1 class='header'>🚗 Calculadora de Ganancias Hoop</h1>
    </div>
""", unsafe_allow_html=True)

# Entradas del usuario
km = st.slider("¿Cuántos kilómetros conduces al mes?", 0, 5000, 1000, step=100)
pasajeros = st.slider("¿Cuántos pasajeros llevas normalmente?", 0, 5, 1)

if km == 0 or pasajeros == 0:
    st.error("Por favor, introduce un número mayor que 0 en ambos campos.")
else:
    # Cálculo de ganancias
    ganancia = km * pasajeros * 0.04
    st.markdown(f"""
        <div class='card'>
            <h2>🎉 Puedes ganar hasta <span style='color:#00a082;'>{ganancia:.2f}€/mes</span> con Hoop</h2>
        </div>
    """, unsafe_allow_html=True)

    # Ganancia anual
    ganancia_anual = ganancia * 12
    st.markdown(f"""
        <div class='card'>
            <h4>💡 Esto equivaldría a <span style='color:#00a082;'>{ganancia_anual:.2f}€/año</span></h4>
        </div>
    """, unsafe_allow_html=True)

    # Mostrar cálculo adicional solo si se elige 1 o más pasajeros
    if pasajeros > 0:
        ganancia_extra = km * (pasajeros + 1) * 0.04
        ganancia_extra_anual = ganancia_extra * 12
        
        # Ganancia con 1 pasajero más (mensual y anual) - tamaño más pequeño
        st.markdown(f"""
            <div class='card'>
                <h3 style='font-size: 1.2rem;'>🚗 Si llevaras 1 pasajero más:</h3>
                <p style='font-size: 1rem;'>Podrías ganar hasta <span style='color:#00a082;'>{ganancia_extra:.2f}€/mes</span></p>
                <h4 style='font-size: 1rem;'>💡 Esto equivaldría a <span style='color:#00a082;'>{ganancia_extra_anual:.2f}€/año</span></h4>
            </div>
        """, unsafe_allow_html=True)

    # Información sobre el Bono Hoop con botón de despliegue (ℹ️)
    with st.expander("ℹ️ ¿Qué es el Bono Hoop?", expanded=False):
        st.markdown("""  
        **El Bono Hoop** es un incentivo económico que te premia por compartir coche y generar ahorro energético certificado.

        🔋 Cada trayecto compartido genera Certificados de Ahorro Energético (CAEs), que Hoop vende a empresas energéticas. A ti te llega ese dinero como **compensación directa en cada viaje**.

        💶 Puedes ganar hasta **1.000 € al año** si cumples con estos pasos:
        - Completa tus datos personales en la app.
        - Registra tu matrícula si eres conductor.
        - Activa la geolocalización y verifica los trayectos.

        📲 El bono se paga los lunes y lo verás en el **monedero de la app**. El incentivo es **compatible con otras ayudas** y **no tributa** si no supera los 1.000 € anuales.

        👉 Solo disponible en España.
        """)

    # Botón de WhatsApp
    mensaje = f"🚗 ¡Estoy ganando hasta {ganancia:.2f}€/mes con Hoop compartiendo coche! Descubre cuánto puedes ganar tú también 👉https://www.hoopcarpool.com/es/descarga-app-hoop-carpool"
    url_whatsapp = f"https://wa.me/?text={urllib.parse.quote(mensaje)}"

    st.markdown(f"""
        <div class='footer'>
            <a class='whatsapp-button' href="{url_whatsapp}" target="_blank">
                📤 Compartir por WhatsApp
            </a>
        </div>
    """, unsafe_allow_html=True)
