import streamlit as st
import os
from PIL import Image

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Marco Metodológico - Trump 2024", page_icon="📂", layout="wide")

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
    
    .metodo-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        border-top: 4px solid #003366;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        height: 100%;
    }
    .finalidad-box {
        background-color: #003366;
        color: white !important;
        padding: 25px;
        border-radius: 15px;
        border-left: 10px solid #FFCC00;
        margin: 20px 0;
    }
    .finalidad-box p { color: white !important; font-style: italic; }
    </style>
    """, unsafe_allow_html=True)


# --- 3. TÍTULO ---
st.markdown("<h1 style='text-align: center; color: #003366 !important;'>📂 Marco Metodológico</h1>", unsafe_allow_html=True)

# --- 4. FINALIDAD DEL MODELO (TEXTO SIMPLE Y LIMPIO) ---
st.markdown("<h3 class='section-title'>Finalidad del Modelo de Regresión</h3>", unsafe_allow_html=True)

st.write(
    "El presente modelo de regresión lineal tiene como finalidad comprender la "
    "**relación funcional** que existe entre el gasto máximo realizado por Donald J. Trump "
    "en las plataformas de Meta (Facebook e Instagram) durante el período de campaña "
    "de las elecciones estadounidenses de 2024 y las impresiones máximas alcanzadas por "
    "Donald J. Trump en estas mismas plataformas."
)

st.write(
    "Todas las técnicas e inferencias que se aplicarán en el presente trabajo se presentan "
    "a nivel teórico en el **Capítulo II (Marco Teórico)** y se emplean en el **Capítulo IV**."
)

st.markdown("---") # Una línea sutil para separar de la siguiente sección

# --- 5. NATURALEZA DE LA INVESTIGACIÓN ---
st.markdown("<h3 class='section-title'>1. Naturaleza de la Investigación</h3>", unsafe_allow_html=True)

col_a, col_b = st.columns(2)
with col_a:
    st.markdown("""
    <div class="metodo-card">
        <h4>🔬 Tipo y Nivel</h4>
        <ul>
            <li><b>Investigación Documental:</b> Basada en la búsqueda, recuperación y análisis de datos secundarios registrados en la <i>Meta Ads Library</i>.</li>
            <li><b>Nivel Correlacional:</b> Analiza la relación entre el Gasto Estimado ($X$) y las Impresiones Máximas ($Y$).</li>
            <li><b>Alcance Explicativo:</b> Orientado a comprender la idoneidad del MRLS para explicar el fenómeno de la visibilidad publicitaria.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
with col_b:
    st.markdown("""
    <div class="metodo-card">
        <h4>📋 Diseño de Investigación</h4>
        <p>Se suscribe a un diseño <b>No Experimental - Transeccional</b>. El estudio observa las variables en su contexto natural (Campaña Electoral 2024) sin manipulación deliberada de los datos.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 7. UNIVERSO Y MUESTREO ---
st.markdown("<h3 class='section-title'>2. Población y Muestreo</h3>", unsafe_allow_html=True)

col_u, col_m, col_t = st.columns(3)
with col_u:
    st.markdown("""<div class="metodo-card" style="border-top-color: #FFCC00;"><h4>🌌 Universo</h4><p style="font-size: 2rem !important; text-align: center; font-weight: bold; color: #003366;">59.500</p><p style="text-align: center;"> Anuncios publicitarios registrados en el Meta Ads Library difundidos a través de Facebook e Instagram durante la campaña electoral de Estados Unidos de 2024 por el anunciante Donald J. Trump. </p></div>""", unsafe_allow_html=True)
with col_m:
    st.markdown("""<div class="metodo-card" style="border-top-color: #FFCC00;"><h4>📊 Muestra</h4><p style="font-size: 2rem !important; text-align: center; font-weight: bold; color: #003366;">2.000</p><p style="text-align: center;"> Anuncios publicitarios registrados en el Meta Ads Library difundidos a través de Facebook e Instagram durante la campaña electoral de Estados Unidos de 2024 por el anunciante Donald J. Trump. </p></div>""", unsafe_allow_html=True)
with col_t:
    st.markdown("""<div class="metodo-card" style="border-top-color: #FFCC00;"><h4>🎯 Tipo de Muestreo</h4><p><b>Aleatorio Simple (M.A.S.)</b></p><p> Se implementó un script de Python que seleccionó 2.000 registros únicos filtrándolos por su identificador único de anuncio para garantizar la representatividad estadística del subconjunto analizado con respecto a la población original. </p></div>""", unsafe_allow_html=True)

# --- 8. VARIABLES Y ECUACIÓN DEL MODELO ESTIMADO ---
st.markdown("<h3 class='section-title'>3. Definición del Modelo Estadístico</h3>", unsafe_allow_html=True)

col_var, col_eq = st.columns([1, 1.2])

with col_var:
    st.write("**Variables del Estudio:**")
    st.latex(r"\hat{x}: \text{ Gasto máximo en dólares (Variable Independiente)}")
    st.latex(r"\hat{y}: \text{ Impresiones máximas (Variable Dependiente)}")

with col_eq:
    st.write("**Ecuación del Modelo de Regresión Lineal Estimado:**")
    # Caja resaltada para la fórmula exacta de tu imagen
    st.info("El modelo estimado se define como:")
    st.latex(r"\hat{y} = a + bx")
    
    st.write("**Donde:**")
    st.markdown(r"- $\hat{y}$: Valor estimado de la variable dependiente (Impresiones).")
    st.markdown(r"- $a$: Ordenada en el origen (punto donde la recta corta el eje Y).")
    st.markdown(r"- $b$: Coeficiente de regresión (pendiente de la recta).")
    st.markdown(r"- $x$: Valor de la variable independiente (Gasto).")

st.markdown("---")
st.caption("Nota: Los valores de 'a' y 'b' se obtienen mediante el procedimiento de Mínimos Cuadrados para minimizar el error residual.")