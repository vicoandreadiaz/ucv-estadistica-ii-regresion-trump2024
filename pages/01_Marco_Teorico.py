import streamlit as st
import os
from PIL import Image

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Marco Teórico - Trump 2024", page_icon="📖", layout="wide")

# --- 2. ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp { background-color: white !important; color: #31333F !important; }
    .stMarkdown, p, li, h1, h2, h3, h4, h5, h6, span { color: #31333F !important; }
    p, li, .stMarkdown { font-size: 1.2rem !important; line-height: 1.6 !important; }
    .section-title { color: #003366 !important; border-bottom: 2px solid #ccc; padding-bottom: 5px; margin-top: 30px; margin-bottom: 20px; font-weight: bold; }
    .ucv-text { color: #003366 !important; padding-top: 10px; border-bottom: 2px solid #FFCC00; padding-bottom: 10px; margin-bottom: 15px; }
    .ucv-text h4 { margin: 0; font-size: 1.4rem; font-weight: bold; color: #003366 !important;}
    .ucv-text h5 { margin: 0; font-size: 1.1rem; color: #555 !important;}
    .tarjeta-destacada { background-color: #f1f8ff !important; border-left: 6px solid #FFCC00 !important; border-right: 6px solid #003366 !important; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }
    .tarjeta-destacada h3 { color: #003366 !important; margin-top: 0; }
    .supuesto-box { background-color: #f8f9fa; border-left: 4px solid #003366; padding: 15px; border-radius: 5px; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. TÍTULO Y MÉTRICAS ---
st.markdown("<h1 style='text-align: center; color: #003366 !important;'> Marco Teórico y Conceptual</h1>", unsafe_allow_html=True)
st.write("Un anuncio de Meta es una forma de publicidad política pagada que permite a las empresas mostrar mensajes promocionales, imágenes o vídeos a audiencias específicas en las plataformas de Meta. Estas herramientas utilizan inteligencia artificial y segmentación detallada (demografía, intereses, comportamientos) para conectar con clientes potenciales.")

# Aquí están los botones con sus íconos
btn_fb, btn_ig, btn_wa, btn_ms = st.tabs(["📘 Facebook", "📸 Instagram", "💬 WhatsApp", "⚡ Messenger"])

with btn_fb:
    st.info("**Facebook (La Base de Datos Principal):** Es el núcleo de la publicidad política. Gracias a su madurez, posee la mayor cantidad de datos demográficos y psicográficos. Es la plataforma ideal para la movilización de bases, recaudación de fondos y difusión de mensajes largos o videos explicativos. Atrae predominantemente a votantes de mayor edad.")
with btn_ig:
    st.info("**Instagram (El Impacto Visual):** Se centra en el contenido visual, la estética y la inmediatez (Reels, Historias). En la publicidad política, es la herramienta principal para humanizar al candidato, mostrar el 'detrás de escena' de las giras y captar la atención del electorado joven.")
with btn_wa:
    st.info("**WhatsApp (La Comunicación Directa):** Aunque no muestra 'anuncios' tradicionales en los chats, el ecosistema de Meta permite crear anuncios en Facebook e Instagram cuyo botón redirige directamente a un chat de WhatsApp con el equipo de campaña, facilitando el activismo local.")
with btn_ms:
    st.info("**Audience Network & Messenger (La Extensión):** Los anuncios políticos también se distribuyen en las bandejas de entrada de Messenger y a través de una red de miles de aplicaciones de terceros, lo que permite perseguir al votante (retargeting) incluso cuando cierra las redes sociales.")

st.write("") # Espaciador

st.markdown("<h3 class='section-title'>1. Métricas que se pueden obtener en Meta Ads</h3>", unsafe_allow_html=True)

st.markdown("""
<div class="tarjeta-destacada">
    <h3> IMPRESIONES (Nuestra Variable Dependiente 'Y')</h3>
    <p style="font-size: 1.3rem !important;"><b>Significado:</b> El número total de veces que el anuncio se mostró en pantalla, independientemente de si fue a la misma persona varias veces.</p>
</div>
""", unsafe_allow_html=True)

st.write("Selecciona una dimensión para explorar el resto de métricas involucradas en la publicidad política:")

tab1, tab2, tab3, tab4 = st.tabs(["Entrega y Visibilidad", "Interacción y Tráfico", "Costo y Eficiencia", "Conversión y Retorno"])
with tab1:
    with st.expander("Alcance"): st.write("El número de personas únicas e individuales a las que se les mostró el anuncio al menos una vez.")
    with st.expander("Frecuencia"): st.write("El promedio de veces que cada persona alcanzó a ver el anuncio (Impresiones divididas entre el Alcance).")
with tab2:
    with st.expander("Clics en el enlace"): st.write("La cantidad de clics que efectivamente dirigen al usuario fuera del anuncio hacia tu destino.")
    with st.expander("CTR (Click-Through Rate)"): st.write("El porcentaje de personas que vieron el anuncio y decidieron hacer clic en el enlace. Mide el atractivo de la creatividad.")
    with st.expander("Visitas a la página de destino"): st.write("Confirma que el usuario no solo hizo clic, sino que esperó a que tu sitio web cargara por completo.")
with tab3:
    st.info("💰 **CPM (Costo por 1,000 impresiones):** Lo que la plataforma te cobra en promedio por mostrar tu anuncio mil veces. Sirve para medir el nivel de competencia en la subasta.")
    with st.expander("CPC (Costo por Clic)"): st.write("El costo promedio que pagas por cada clic en el enlace de tu anuncio.")
    with st.expander("CPA (Costo por Adquisición)"): st.write("El costo promedio que te toma lograr el objetivo principal de la campaña.")
with tab4:
    with st.expander("Resultados"): st.write("La cantidad total de veces que se completó el objetivo configurado para la campaña.")
    with st.expander("ROAS (Return on Ad Spend)"): st.write("El retorno de inversión publicitaria. Indica cuánto dinero en ingresos generó la campaña por cada unidad monetaria invertida.")

# --- 5. SUPUESTOS DEL MODELO ---
st.markdown("<h3 class='section-title'>2. Supuestos del Modelo</h3>", unsafe_allow_html=True)
st.write("Los supuestos bajo los cuales se rige este modelo de regresión son específicamente los siguientes:")

st.info(r"**1. Independiente-Variable-Fijo:** La variable independiente $X$ es fija, es decir, toma valores que son fijados (escogidos o predeterminados) por el investigador. Este supuesto implica que para cada valor fijo de $X$ hay una distribución de valores $Y$ por probabilidades, llamada subpoblación de $Y$.")

st.info(r"**2. Normalidad del Error:** $E_i$ es una variable aleatoria que se distribuye normalmente con $E(E_i) = 0$, donde $E_i \sim N(0, \sigma^2)$.")

st.info(r"**3. Criterio de Homocedasticidad:** La varianza condicional de $Y$ dado $X$ se llama varianza de la regresión, $\sigma^2_{Y|X}$, y se supone constante para todo valor de $X$, y es igual a la varianza de $E_i$, es decir, $\sigma^2_e$.")

st.info(r"**4. Independencia:** $E_i$ es estadísticamente independiente de $X_i$, porque cada $E_i$ es una muestra aleatoria simple de tamaño uno de una población $N(0, \sigma^2)$.")