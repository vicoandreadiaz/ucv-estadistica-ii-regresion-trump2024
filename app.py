import streamlit as st
import os
from PIL import Image

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Trump 2024 - UCV",
    page_icon="📊",
    layout="wide"
)

# --- 2. ESTILOS CSS (Estética de Presentación) ---
st.markdown("""
    <style>
    /* Agrandar el texto base para la presentación */
    p, li, .stMarkdown {
        font-size: 1.25rem !important;
        line-height: 1.6 !important;
        color: #333333;
    }
    .section-title {
        color: #003366;
        border-bottom: 2px solid #ccc;
        padding-bottom: 5px;
        margin-top: 40px;
        margin-bottom: 20px;
        font-weight: bold;
    }
    .ucv-text {
        color: #003366;
        padding-top: 10px;
        border-bottom: 2px solid #FFCC00;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }
    .ucv-text h4 { margin: 0; font-size: 1.4rem; font-weight: bold;}
    .ucv-text h5 { margin: 0; font-size: 1.1rem; color: #555;}
    
    /* Estilo para los integrantes (Fotos circulares) */
    .integrante-card {
        text-align: center;
        padding: 20px;
    }
    .integrante-card img {
    border-radius: 50%; 
    width: 150px;          
    height: 150px;         
    aspect-ratio: 1 / 1;   
    object-fit: cover;     
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    margin-bottom: 15px;
    display: block;        
    margin-left: auto;     
    margin-right: auto;
    }
    .integrante-card h4 {
        color: #003366;
        margin-bottom: 2px;
        font-weight: bold;
    }
    .integrante-card p {
        color: #666 !important;
        font-size: 1.1rem !important;
    }
    
    /* Estilos para las tarjetas de comparación */
    .metric-container {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #003366;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        height: 100%;
    }
    .metric-blue { border-left-color: #005A9C; } 
    .metric-red { border-left-color: #E81B23; }  
    </style>
    """, unsafe_allow_html=True)

# --- 3. ENCABEZADO: LOGO ESQUINADO Y MEMBRETE ---
col_logo, col_texto = st.columns([1, 8])

with col_logo:
    try:
        st.image("data/assets/logo_ucv.png", width=80)
    except FileNotFoundError:
        st.error("Falta logo_ucv.png")

with col_texto:
    st.markdown("""
    <div class="ucv-text">
        <h4>UNIVERSIDAD CENTRAL DE VENEZUELA</h4>
        <h5>FACULTAD DE CIENCIAS ECONÓMICAS Y SOCIALES | ESCUELA DE ESTADÍSTICA Y CIENCIAS ACTUARIALES</h5>
    </div>
    """, unsafe_allow_html=True)

# --- 4. BANNER PRINCIPAL ---
# Ahora forzamos a que se muestre, o te avise exactamente si la ruta está mal
try:
    st.image("data/assets/banner.png", use_container_width=True)
except FileNotFoundError:
    st.error("🚨 ERROR: No se encuentra la imagen del banner. Asegúrate de que el archivo se llame EXACTAMENTE 'tu_banner.png' y esté guardado dentro de la carpeta 'data/assets/'.")

# --- 5. PLANTEAMIENTO DEL PROBLEMA (TEXTO ORIGINAL) ---
st.markdown("<h3 class='section-title'>1. La evolución de la obtención de métricas en la publicidad política</h3>", unsafe_allow_html=True)
st.write("""
Históricamente, cuando la radio, la televisión y las vallas publicitarias predominaban como canales de comunicación predeterminados para el desenvolvimiento de las campañas electorales, era técnicamente imposible plantearse la tarea de estimar con rigor el alcance real de un anuncio publicitario ó predecir con un margen de error mínimo el volumen de su impacto.

Sin embargo, actualmente, en la era en la que predominan por encima de cualquier medio las plataformas digitales (como las redes sociales), se ha habilitado, gracias a las políticas de transparencia, rendición de cuentas y autenticidad de Meta Platforms, un escenario en el que es posible transformar la incertidumbre a la hora de la toma de decisiones con respecto al gasto a realizar en campañas digitales en una tarea de proyección estadística.
""")

# --- 6. EL ESCENARIO (EL BLOQUE REEMPLAZADO VISUALMENTE) ---
st.markdown("<h3 class='section-title'>2. El escenario de las elecciones de 2024 y la brecha de inversión</h3>", unsafe_allow_html=True)

col_trump, col_biden = st.columns(2)

with col_trump:
    st.markdown("""
    <div class="metric-container metric-red">
        <h3 style="color: #E81B23; margin-top: 0;">🔴 Campaña Donald Trump</h3>
        <h2 style="margin-top: 0;">$ 23,912,674</h2>
        <h4 style="margin-bottom: 0;">Impresiones Totales</h4>
        <h2 style="margin-top: 0;">828,310,808</h2>
    </div>
    """, unsafe_allow_html=True)

with col_biden:
    st.markdown("""
    <div class="metric-container metric-blue">
        <h3 style="color: #005A9C; margin-top: 0;">🔵 Campaña Biden / Harris</h3>
        <h2 style="margin-top: 0;">$ 140,446,791</h2>
        <h4 style="margin-bottom: 0;">Impresiones Totales</h4>
        <h2 style="margin-top: 0;">5,186,759,078</h2>
    </div>
    """, unsafe_allow_html=True)

st.write("") # Espaciador

# Tu justificación resaltada
st.success("""
La inversión de Donald Trump, aunque significativamente menor que la de sus oponentes en cifras absolutas, resultó en la victoria presidencial de 2024, es por ello, que surge la necesidad de entender la eficiencia del gasto; teniendo en cuenta que en términos económicos los demócratas superaron por una gran diferencia su capacidad de inversión y, aún así, el total gastado en publicidad dentro de las plataformas de Meta no aseguró la victoria de la coalición Biden-Harris.
""")


# --- 7. PREGUNTA Y OBJETIVOS (TEXTO ORIGINAL) ---
st.markdown("<h3 class='section-title'>3. Pregunta de Investigación</h3>", unsafe_allow_html=True)
st.info("""
**¿La relación entre el gasto estimado máximo y las impresiones máximas alcanzadas por Trump en la campaña de 2024 puede explicarse a través de un modelo de regresión lineal, siendo esta la forma más óptima de representar ése fenómeno económico?**
""")

st.markdown("<h3 class='section-title'>4. Objetivos de la Investigación</h3>", unsafe_allow_html=True)
st.markdown("#### Objetivo General")
st.write("""
Determinar si la relación entre el gasto estimado máximo y las impresiones máximas alcanzadas por Trump en la campaña de 2024 puede explicarse a través de un modelo de regresión lineal con la finalidad de comprobar si este modelo es el más idóneo para representar éste fenómeno económico.
""")

st.markdown("#### Objetivos Específicos")
with st.expander("Desplegar los 10 Objetivos Específicos"):
    st.write("""
    1. Recopilar los datos para el análisis a través de las plataformas de Meta para el periodo de elecciones de Estados Unidos (2024) del anunciante Donald J. Trump.
    2. Calcular las estadísticas descriptivas de las variables de gasto estimado máximo e impresiones máximas de la campaña de Donald Trump en 2024 para obtener una comprensión preliminar de las mismas.
    3. Construir un diagrama de dispersión para visualizar la forma y dirección de la relación entre el gasto estimado y las impresiones alcanzadas.
    4. Verificar los supuestos del Modelo de Regresión Lineal Simple (MRLS) para validar su aplicación a este fenómeno económico-político.
    5. Estimar los coeficientes de regresión y la ecuación de regresión muestral que modelan este fenómeno económico-político.
    6. Interpretar el significado de los coeficientes de regresión y de la ecuación de regresión muestral en el contexto de la publicidad política digital.
    7. Realizar inferencias estadísticas acerca de los coeficientes de regresión poblacional y del coeficiente de correlación poblacional para determinar si existe una relación lineal significativa.
    8. Calcular la estimación por intervalo para la recta de regresión poblacional y para un valor particular de impresiones.
    9. Estimar y analizar el Coeficiente de Determinación del modelo.
    10. Generar la Tabla ANOVA para evaluar la bondad de ajuste y el poder explicativo del modelo de regresión en términos de variabilidad.
    """)

st.markdown("---")

# --- 8. EQUIPO DE INVESTIGACIÓN ---
st.markdown("<h3 style='text-align: center; color: #003366;'>Equipo de Investigación</h3>", unsafe_allow_html=True)

col_vacia1, col_vic1, col_vic2, col_vacia2 = st.columns([2, 2, 2, 2])

with col_vic1:
    st.markdown('<div class="integrante-card">', unsafe_allow_html=True)
    try:
        st.image("data/assets/victoria.png")
    except FileNotFoundError:
        st.markdown('<img src="https://via.placeholder.com/150" alt="Victoria">', unsafe_allow_html=True)
    st.markdown("""
        <h4>Victoria Díaz</h4>
        <p>Estadística - UCV</p>
        </div>
        """, unsafe_allow_html=True)

with col_vic2:
    st.markdown('<div class="integrante-card">', unsafe_allow_html=True)
    try:
        st.image("data/assets/vicente.png")
    except FileNotFoundError:
        st.markdown('<img src="https://via.placeholder.com/150" alt="Vicente">', unsafe_allow_html=True)
    st.markdown("""
        <h4>Vicente Díaz</h4>
        <p>Estadística - UCV</p>
        </div>
        """, unsafe_allow_html=True)