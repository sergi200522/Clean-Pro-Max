import streamlit as st
import urllib.parse

# Configuración de la página (Pestaña del navegador)
st.set_page_config(
    page_title="Clean Pro Max | Limpieza Profesional",
    page_icon="✨",
    layout="centered"
)

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main-title { font-size: 40px; font-weight: bold; color: #1E3A8A; text-align: center; }
    .subtitle { font-size: 20px; color: #4B5563; text-align: center; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
st.markdown('<p class="main-title">✨ ¡Dejamos tus Espacios Como Nuevos! ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Servicio profesional de lavado, desinfección y pulido a domicilio</p>', unsafe_allow_html=True)

# Imagen principal
st.image("https://images.unsplash.com/photo-1581578731548-c64695cc6952?q=80&w=1200", use_container_width=True)

st.write("---")

# --- NUESTROS SERVICIOS ---
st.header("🧽 Nuestros Servicios Especializados")
st.write("Utilizamos tecnología avanzada y productos de alta calidad para cuidar y renovar cada rincón de tu hogar o negocio.")

# Primera fila de servicios (Muebles y Tapetes)
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://images.unsplash.com/photo-1555041469-a586c61ea9bc?q=80&w=400", caption="Sillones y Sofás")
    st.markdown("**Lavado de Sillones**")
    st.write("Eliminación de manchas profundas y desinfección de todo tipo de telas.")

with col2:
    st.image("https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?q=80&w=400", caption="Sillas de Comedor / Oficina")
    st.markdown("**Sillas y Bancos**")
    st.write("Limpieza a detalle para que tus sillas luzcan impecables nuevamente.")
with col3:
    st.image("https://images.unsplash.com/photo-1600121848594-d8644e57abab?q=80&w=400", caption="Tapetes y Alfombras")
    st.markdown("**Tapetes y Alfombras**")
    st.write("Tratamiento especial para cuidar las fibras y revivir los colores.")

st.write("---")

# --- FORMULARIO DE COTIZACIÓN ---
st.header("📅 Cotiza tu Servicio por WhatsApp")
st.write("Déjanos tus datos y las piezas que deseas limpiar para generar tu presupuesto instantáneo.")

# Crear el formulario
with st.form("formulario_contacto", clear_on_submit=False):
    nombre = st.text_input("Nombre Completo:")
    telefono = st.text_input("Tu Número de Teléfono / WhatsApp:")
    
    servicios_interes = st.multiselect(
        "¿Qué te gustaría cotizar? (Puedes seleccionar varios)",
        ["Sillón / Sofá", "Sillas", "Tapetes / Alfombras", "Colchones", "Interiores de auto"]
    )
    
    detalles = st.text_area("Cuéntanos más detalles (ej. número de plazas, metros cuadrados de mármol o tipo de mueble):")
    
    boton_enviar = st.form_submit_button("Enviar Solicitud por WhatsApp 📲")

# --- LÓGICA DE ENVÍO A WHATSAPP ---
if boton_enviar:
    if nombre and telefono and servicios_interes:
        # 🚨 REEMPLAZA ESTE NÚMERO: Pon tu celular real (Ej: "525512345678" para México) sin espacios ni el signo +
        NUMERO_WHATSAPP = "525549657817" 
        
        texto_mensaje = (
            f"¡Hola! Me gustaría una cotización.\n\n"
            f"👤 *Nombre:* {nombre}\n"
            f"📞 *Teléfono:* {telefono}\n"
            f"🧽 *Servicios:* {', '.join(servicios_interes)}\n"
            f"📝 *Detalles:* {detalles if detalles else 'Ninguno'}"
        )
        
        mensaje_codificado = urllib.parse.quote(texto_mensaje)
        url_whatsapp = f"https://wa.me/{NUMERO_WHATSAPP}?text={mensaje_codificado}"
        
        st.success("¡Formulario procesado con éxito!")
        st.link_button("👉 Enviar cotización por WhatsApp", url_whatsapp, type="primary")
    else:
        st.error("Por favor, llena los campos obligatorios antes de enviar.")

# --- PIE DE PÁGINA ---
st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>📍 Cobertura en toda la ciudad | ⏰ Lunes a Sábado de 9:00 AM a 6:00 PM</p>", unsafe_allow_html=True)
