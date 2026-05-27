import streamlit as st

# Configuración de la página (Pestaña del navegador)
st.set_page_config(
    page_title="Limpieza Profesional de Tapicería",
    page_icon="✨",
    layout="centered"
)

# --- ESTILOS PERSONALIZADOS (Opcional, para darle un toque de color) ---
st.markdown("""
    <style>
    .main-title { font-size: 40px; font-weight: bold; color: #1E3A8A; text-align: center; }
    .subtitle { font-size: 20px; color: #4B5563; text-align: center; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
st.markdown('<p class="main-title">✨ ¡Dejamos tus Muebles Como Nuevos! ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Servicio profesional de lavado y desinfección a domicilio</p>', unsafe_allow_html=True)

# Imagen principal / Banner (Puedes cambiar la URL por una foto de tu negocio)
st.image("https://images.unsplash.com/photo-1581578731548-c64695cc6952?q=80&w=1200", use_container_width=True)

st.write("---")

# --- NUESTROS SERVICIOS ---
st.header("🧽 Nuestros Servicios")
st.write("Utilizamos tecnología de inyección-succión y productos biodegradables que eliminan manchas, ácaros y malos olores.")

# Crear 3 columnas para mostrar los servicios principales
col1, col2, col3 = st.columns(3)

with col1:
    # Reemplaza estas URLs con fotos reales de tus trabajos de sillones
    st.image("https://images.unsplash.com/photo-1555041469-a586c61ea9bc?q=80&w=400", caption="Sillones y Sofás")
    st.markdown("*Lavado de Sillones*")
    st.write("Eliminación de manchas profundas y desinfección de todo tipo de telas.")

with col2:
    # Reemplaza con foto de sillas
    st.image("https://images.unsplash.com/photo-1503602642458-232111445657?q=80&w=400", caption="Sillas de Comedor / Oficina")
    st.markdown("*Sillas y Bancos*")
    st.write("Limpieza a detalle para que tus sillas luzcan impecables nuevamente.")

with col3:
    # Reemplaza con foto de tapetes
    st.image("https://images.unsplash.com/photo-1600121848594-d8644e57abab?q=80&w=400", caption="Tapetes y Alfombras")
    st.markdown("*Tapetes y Alfombras*")
    st.write("Tratamiento especial para cuidar las fibras y revivir los colores.")

st.write("---")

# --- FORMULARIO DE COTIZACIÓN ---
st.header("📅 Cotiza tu Servicio Gratis")
st.write("Déjanos tus datos y las piezas que deseas limpiar. Te contactaremos de inmediato.")

# Crear el formulario
with st.form("formulario_contacto", clear_on_submit=True):
    nombre = st.text_input("Nombre Completo:")
    telefono = st.text_input("Número de Teléfono / WhatsApp:")
    
    # Opciones de servicios
    servicios_interes = st.multiselect(
        "¿Qué te gustaría limpiar? (Puedes seleccionar varios)",
        ["Sillón / Sofá", "Sillas de comedor", "Sillas de oficina", "Tapetes", "Colchones", "Interiores de auto"]
    )
    
    detalles = st.text_area("Cuéntanos más detalles (ej. 'sofá de 3 plazas con manchas de café', 'tapete de 2x3 metros'):")
    
    # Botón de envío
    boton_enviar = st.form_submit_button("Enviar Solicitud 🚀")

# --- LÓGICA DE ENVÍO A WHATSAPP ---
if boton_enviar:
    if nombre and telefono and servicios_interes:
        # 🚨 CAMBIA ESTE NÚMERO POR EL TUYO REAL (Ej: "5215512345678" -> Código país + número sin espacios ni +)
        NUMERO_WHATSAPP = "55 4965 7817" 
        
        # Estructuramos el mensaje de texto ordenado para tu WhatsApp
        texto_mensaje = (
            f"¡Hola! Me gustaría una cotización.\n\n"
            f"👤 Nombre: {nombre}\n"
            f"📞 Teléfono: {telefono}\n"
            f"🧽 Servicios: {', '.join(servicios_interes)}\n"
            f"📝 Detalles: {detalles if detalles else 'Ninguno'}"
        )
        
        # Codificamos el texto para que la URL funcione en internet de forma segura
        import urllib.parse
        mensaje_codificado = urllib.parse.quote(texto_mensaje)
        url_whatsapp = f"https://wa.me/{NUMERO_WHATSAPP}?text={mensaje_codificado}"
        
        # Mostramos el botón azul brillante para redirigir al cliente
        st.success("¡Formulario procesado con éxito!")
        st.link_button("👉 Enviar cotización por WhatsApp", url_whatsapp, type="primary")
    else:
        st.error("Por favor, llena los campos obligatorios antes de enviar.")

# --- PIE DE PÁGINA ---
st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>📍 Cobertura en toda la ciudad | ⏰ Lunes a Sábado de 9:00 AM a 6:00 PM</p>", unsafe_allow_html=True)
