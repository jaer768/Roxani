import streamlit as st
import streamlit.components.v1 as components

# Configuración inicial
st.set_page_config(page_title="Necesidad Futura - Camposanto", layout="wide", page_icon="🌿")

# Título y descripción
st.title("🌿 Programa de Necesidad Futura")
st.markdown("""
Bienvenido al sitio informativo sobre el **Programa de Necesidad Futura** del *Camposanto Parque del Recuerdo* y *Jardines del Buen Retiro*.  
Este programa ha sido diseñado para brindarte **tranquilidad, previsión y respaldo familiar** en los momentos más difíciles.

---

### 🏞️ ¿Qué es el Programa de Necesidad Futura?
El programa consiste en adquirir hoy un servicio funerario integral para el futuro, con facilidades de pago, asesoría personalizada y cobertura garantizada.

""")

# Video institucional embebido
st.subheader("🎬 Conoce el programa")
components.html(
    """
    <iframe width="100%" height="400" src="https://www.youtube.com/embed/1aWZFw0ccHE" 
    title="Video institucional" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
    encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    """,
    height=420
)

# Imagen de referencia
st.subheader("📸 Camposanto & Jardines")
st.image(
    "https://www.parquedelrecuerdo.pe/wp-content/uploads/2021/09/header-inicio.jpg",
    caption="Vista panorámica del Camposanto Parque del Recuerdo",
    use_container_width=True
)

# Ventajas del programa
st.header("🌟 Ventajas del Programa de Necesidad Futura")
st.markdown("""
- ✅ **Previsión familiar:** evitas decisiones apresuradas en momentos difíciles.
- ✅ **Facilidades de pago:** financiamiento flexible sin intereses.
- ✅ **Ahorro garantizado:** precios actuales, sin incrementos futuros.
- ✅ **Cobertura total:** asistencia integral desde el traslado hasta el sepelio.
- ✅ **Ubicación preferencial:** acceso a los mejores espacios y jardines conmemorativos.
""")

# Datos de la asesora
st.header("📞 Tu asesora de confianza")
st.markdown("""
**Roxani Ramírez Sánchez**  
Consejera del Programa de Necesidad Futura  
📱 **Teléfono:** [992774074](tel:+51992774074)
""")

st.info("Puedes comunicarte directamente con Roxani para agendar una visita o recibir asesoría personalizada.")

# Cuestionario de contacto
st.header("✍️ ¿Te interesa recibir más información?")

with st.form("contact_form"):
    nombre = st.text_input("Nombre completo")
    telefono = st.text_input("Teléfono de contacto")
    correo = st.text_input("Correo electrónico")
    distrito = st.text_input("Distrito de residencia")
    interes = st.selectbox("¿Qué servicio te interesa conocer?", [
        "Terreno familiar",
        "Servicios funerarios",
        "Planes a futuro",
        "Otros"
    ])
    comentario = st.text_area("Comentario o consulta adicional")

    enviado = st.form_submit_button("Enviar contacto")

    if enviado:
        st.success("✅ ¡Gracias por tu interés! Nos pondremos en contacto contigo pronto.")

        # Aquí podrías almacenar los datos en una base de datos o enviarlos por correo
        st.write("**Resumen de tus datos:**")
        st.write(f"👤 Nombre: {nombre}")
        st.write(f"📞 Teléfono: {telefono}")
        st.write(f"📧 Correo: {correo}")
        st.write(f"📍 Distrito: {distrito}")
        st.write(f"📝 Interés: {interes}")
        st.write(f"💬 Comentario: {comentario}")
