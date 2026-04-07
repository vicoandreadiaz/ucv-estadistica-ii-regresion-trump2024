import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Resultados Finales - Trump 2024", page_icon="📈", layout="wide")

# --- 2. ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp { background-color: white; }
    .section-title { color: #003366; border-bottom: 2px solid #FFCC00; padding-bottom: 5px; margin-top: 40px; margin-bottom: 20px; font-weight: bold; border-left: 10px solid #003366; padding-left: 15px; }
    .spss-box { background-color: #ffffff; border: 1px solid #e6e9ef; border-radius: 10px; padding: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 100%; }
    .canavos-note { font-style: italic; color: #555; border-left: 3px solid #ccc; padding-left: 15px; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #003366;'>📈 Análisis de Regresión Lineal Bivariante - SPSS</h1>", unsafe_allow_html=True)
st.write("A continuación se presentan los resultados inferenciales extraídos de IBM SPSS, estructurados para validar paso a paso la relación entre el gasto y el alcance publicitario.")

# =====================================================================
# SECCIÓN 1: CORRELACIÓN (NUEVA SECCIÓN)
# =====================================================================
st.markdown("<h3 class='section-title'>1. Análisis de Correlación Bivariada</h3>", unsafe_allow_html=True)
col_corr1, col_corr2 = st.columns([1.5, 1])

with col_corr1:
    st.markdown('<div class="spss-box">', unsafe_allow_html=True)
    st.image("data/assets/spss_correlacion.png", caption="Output: Matriz de Correlación de Pearson", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_corr2:
    st.markdown("#### Coeficiente de Pearson ($r$)")
    st.latex(r"r = 0,903 \quad (p < 0,001)")
    st.success("Existe una **correlación lineal positiva muy fuerte** entre el Gasto Estimado y las Impresiones.")
    st.write("Este resultado inicial justifica la pertinencia de avanzar hacia un modelo de regresión, confirmando que a mayor inversión, el alcance tiende a crecer de forma estadísticamente consistente.")

# =====================================================================
# SECCIÓN 2: ESTIMACIÓN Y SIGNIFICANCIA
# =====================================================================
st.markdown("<h3 class='section-title'>2. Significancia Global y Bondad de Ajuste</h3>", unsafe_allow_html=True)

col_res, col_ano = st.columns(2)
with col_res:
    st.markdown('<div class="spss-box">', unsafe_allow_html=True)
    st.image("data/assets/spss_resumen.png", caption="Output: Resumen del Modelo", use_container_width=True)
    st.markdown("""<p class="canavos-note">El R² (0,843) indica que el modelo explica el 84,3% de la variabilidad, pero no certifica la validez estructural de la linealidad (Canavos).</p>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_ano:
    st.markdown('<div class="spss-box">', unsafe_allow_html=True)
    st.image("data/assets/spss_anova.png", caption="Output: Tabla ANOVA", use_container_width=True)
    st.info("La prueba F arroja un nivel de significancia menor a 0,05, por lo que se rechaza la hipótesis nula: **el modelo tiene capacidad predictiva válida**.")
    st.markdown('</div>', unsafe_allow_html=True)

# =====================================================================
# SECCIÓN 3: ECUACIÓN DEL MODELO
# =====================================================================
st.markdown("<h3 class='section-title'>3. Coeficientes y Recta Estimada</h3>", unsafe_allow_html=True)

col_coef, col_eq = st.columns([1.5, 1])
with col_coef:
    st.markdown('<div class="spss-box">', unsafe_allow_html=True)
    st.image("data/assets/spss_coeficientes.png", caption="Output: Coeficientes de Regresión", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_eq:
    st.markdown("#### Ecuación Resultante")
    st.latex(r"\hat{y} = 2368,407 + 26,299x")
    st.write("**Lectura de parámetros:**")
    st.markdown(r"- **Constante ($a$):** 2368 impresiones máximas.")
    st.markdown(r"- **Pendiente ($b$):** **+26,3 impresiones** máximas por cada dólar invertido.")

# =====================================================================
# SECCIÓN 4: SIMULADOR
# =====================================================================
st.markdown("<h3 class='section-title'>4. Simulador de Inversión / Retorno</h3>", unsafe_allow_html=True)
st.write("Pon a prueba el modelo calculando escenarios teóricos:")

c_input, c_res = st.columns(2)
with c_input:
    mode = st.radio("Dirección del cálculo:", ["Proyectar Impresiones (dado el Gasto)", "Estimar Presupuesto (dado el Objetivo)"], horizontal=True)
    if mode == "Proyectar Impresiones (dado el Gasto)":
        val_x = st.number_input("Inversión en campaña (USD):", min_value=0.0, value=5000.0, step=100.0)
        st.success(f"Visibilidad estimada ($\hat{{y}}$): **{2367.288 + (26.299 * val_x):,.0f} impresiones**")
    else:
        val_y = st.number_input("Objetivo de Impresiones:", min_value=0.0, value=100000.0, step=1000.0)
        st.success(f"Inversión requerida ($x$): **${(val_y - 2367.288) / 26.299:,.2f} USD**")

# =====================================================================
# SECCIÓN 5: VERIFICACIÓN DE SUPUESTOS
# =====================================================================
st.markdown("<h3 class='section-title'>5. Verificación de Supuestos</h3>", unsafe_allow_html=True)

col_sup1, col_sup2 = st.columns(2)
with col_sup1:
    st.markdown('<div class="spss-box">', unsafe_allow_html=True)
    st.image("data/assets/spss_normalidad.png", caption="Normalidad de Residuos", use_container_width=True)
    st.error("❌ **Normalidad:** Desviación en las colas. Riesgo en la estimación de intervalos.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_sup2:
    st.markdown('<div class="spss-box">', unsafe_allow_html=True)
    st.image("data/assets/spss_homocedasticidad.png", caption="Dispersión (Homocedasticidad)", use_container_width=True)
    st.error("❌ **Homocedasticidad:** Varianza no constante (efecto embudo).")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div style="background-color: #fff4f4; padding: 15px; border-radius: 8px; border-left: 5px solid #cc0000; margin-top: 10px;">
    <strong>Conclusión Final:</strong> Pese a la altísima correlación y al R cuadrado favorable, la falla sistemática en los supuestos del modelo demuestra que la verdadera relación contiene dinámicas no lineales subyacentes o sufre de sesgos por variables omitidas. El MRLS es referencial, pero no estructuralmente idóneo para este ecosistema digital.
</div>
""", unsafe_allow_html=True)