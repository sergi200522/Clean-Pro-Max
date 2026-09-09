import streamlit as st
import urllib.parse

# Configuración de la página
st.set_page_config(
    page_title="Clean Pro Max",
    page_icon="🧹",
    layout="wide"
)

# --- CONFIGURACIÓN DE WHATSAPP ---
# Sustituye este número por tu número real a 10 dígitos (incluyendo el código de país, ej. 52 para México)
NUMERO_TEL = "525549657817" 

def crear_link_whatsapp(mensaje):
    mensaje_codificado = urllib.parse.quote(mensaje)
    return f"https://wa.me/{NUMERO_TEL}?text={mensaje_codificado}"

# --- BARRA LATERAL / NAVEGACIÓN DESPLEGABLE ---
st.sidebar.title("🧹 Clean Pro Max")
st.sidebar.markdown("---")

opcion_menu = st.sidebar.selectbox(
    "Navega por nuestra página:",
    ["Inicio", "Servicios", "Contacto por WhatsApp"]
)

# --- PÁGINA: INICIO ---
if opcion_menu == "Inicio":
    st.title("Bienvenido a Clean Pro Max 🧹✨")
    st.subheader("Especialistas en la limpieza y cuidado de tus espacios.")
    st.write(
        "Ofrecemos servicios profesionales de mantenimiento para dar vida, "
        "brillo y elegancia a cada rincón de tu hogar u oficina."
    )
    
    st.info("👈 Selecciona **Servicios** en el menú desplegable de la izquierda para ver nuestro catálogo completo.")

# --- PÁGINA: SERVICIOS ---
elif opcion_menu == "Servicios":
    st.title("🛠️ Nuestros Servicios")
    st.write("Explora las opciones de mantenimiento y pulido que tenemos para ti:")
    
    servicio_seleccionado = st.sidebar.radio(
        "Filtrar servicio:",
        ["Todos", "Tratamiento de Madera", "Pulido de Mármol"]
    )
    
    col1, col2 = st.columns(2)
    
    # Mostrar Servicio de Madera
    if servicio_seleccionado in ["Todos", "Tratamiento de Madera"]:
        with col1:
            st.image(
                "https://images.unsplash.com/photo-1581858726788-75bc0f6a952d?q=80&w=500", 
                caption="Tratamiento de Madera"
            )
            st.markdown("### 🪵 Tratamiento de Madera")
            st.write(
                "Eliminamos suciedad acumulada y devolvemos el brillo natural "
                "a tus muebles y pisos de madera."
            )
            msg_madera = "¡Hola! Me interesa solicitar una cotización para el servicio de Tratamiento de Madera."
            st.link_button("🟢 Cotizar Madera por WhatsApp", crear_link_whatsapp(msg_madera))

    # Mostrar Servicio de Mármol
    if servicio_seleccionado in ["Todos", "Pulido de Mármol"]:
        with col2:
            st.image(
                "AQUÍ_PEGA_TU_ENLACE_DIRECTO_DE_POSTIMAGES", 
                caption="Pulido Profesional de Mármol"
            )
            st.markdown("### 🏛️ Pulido y Abrillantado de Mármol")
            st.write(
                "Remoción de rayones y sellado de pisos o cubiertas de mármol "
                "para un acabado espejo."
            )
            msg_marmol = "¡Hola! Me interesa solicitar una cotización para el servicio de Pulido y Abrillantado de Mármol."
            st.link_button("🟢 Cotizar Mármol por WhatsApp", crear_link_whatsapp(msg_marmol))

# --- PÁGINA: CONTACTO POR WHATSAPP ---
elif opcion_menu == "Contacto por WhatsApp":
    st.title("📞 Contacto Directo")
    st.write("Presiona el botón para abrir un chat directo con nosotros:")
    
    msg_general = "¡Hola Clean Pro Max! Quisiera pedir información general sobre sus servicios de limpieza."
    st.link_button("💬 Abrir WhatsApp Chat", crear_link_whatsapp(msg_general))
