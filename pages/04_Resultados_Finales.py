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
st.write("A continuación se presentan los resultados inferenciales extraídos de IBM SPSS, estructurados para validar paso a paso la relación entre el gasto máximo y las impresiones máximas de la campaña de Donald J. Trump (2024).")

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
    st.success("las variables presentan una correlación lineal muy alta, en otras palabras, mientras aumenta el gasto máximo que presente una campaña publicitaria, aumentará de manera notoria las impresiones de la misma campaña.")
    st.write("Este resultado inicial justifica la pertinencia de avanzar hacia un modelo de regresión, confirmando que a mayor inversión, las impresiones tienden a crecer de manera notoria.")

# =====================================================================
# SECCIÓN 2: ESTIMACIÓN Y SIGNIFICANCIA
# =====================================================================
st.markdown("<h3 class='section-title'>2. Significancia Global y Bondad de Ajuste</h3>", unsafe_allow_html=True)

col_res, col_ano = st.columns(2)
with col_res:
    st.markdown('<div class="spss-box">', unsafe_allow_html=True)
    st.image("data/assets/spss_resumen.png", caption="Output: Resumen del Modelo", use_container_width=True)
    st.markdown("""<p class="canavos-note">El R² (0,843) indica que 84,3% la variabilidad del número de impresiones de una campaña publicitaria es explicada por los gastos de dicha campaña. Solo el 15,7% de la variabilidad del número máximo de impresiones se debe a otros factores no incluidos en el modelo, pero no certifica con certeza que sea el modelo que mejor se ajuste a los datos.</p>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_ano:
    st.markdown('<div class="spss-box">', unsafe_allow_html=True)
    st.image("data/assets/spss_anova.png", caption="Output: Tabla ANOVA", use_container_width=True)
    st.info("La prueba F arroja un nivel de significancia menor a 0,05, por lo que se rechaza la hipótesis nula: el modelo de regresión lineal propuesto es estadísticamente significativo, es decir, podemos afirmar que la variable  “Gastos máximos” es un predictor lineal significativo de la variable “Impresiones máximas” con un nivel de significación de 0,05.")
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

st.write("") # Espaciador

# Parte B: El Gráfico de la recta (¡Tu nueva imagen!)
st.markdown("#### Representación Gráfica del Modelo")
col_graf1, col_graf2, col_graf3 = st.columns([1, 2, 1]) # Esto centra la imagen para que se vea elegante
with col_graf2:
    st.markdown('<div class="spss-box">', unsafe_allow_html=True)
    # Aquí se carga la imagen que me pasaste
    st.image("data/assets/spss_grafico_recta.png", caption="Curva de Ajuste Lineal (Gasto vs. Impresiones)", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
# =====================================================================
# SECCIÓN 4: ESTIMACIÓN POR INTERVALO
# =====================================================================
st.markdown("<h3 class='section-title'>4. Estimación por intervalo para la recta $\mu_{y|x}$ y para $Y_a$</h3> para un valor de x = 3999", unsafe_allow_html=True)
col_int1, col_int2 = st.columns(2)

with col_int1:
    st.markdown('<div class="spss-box">', unsafe_allow_html=True)
    st.markdown("#### Intervalo de confianza para $\mu_{y|x}$")
    st.latex(r"104.986,12 \le \mu_{yx} \le 110.088,95")
    st.markdown('</div>', unsafe_allow_html=True)

with col_int2:
    st.markdown('<div class="spss-box">', unsafe_allow_html=True)
    st.markdown("#### Intervalo de confianza para $Y_a$")
    st.latex(r"13.343,54 \le Y_a \le 201.731,53")
    st.markdown('</div>', unsafe_allow_html=True)

# =====================================================================
# SECCIÓN 5: SIMULADOR
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
# SECCIÓN 6: VERIFICACIÓN DE SUPUESTOS
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
    <strong>Conclusión Final:</strong> El análisis realizado permite determinar que, si bien el Modelo de Regresión Lineal Simple (MRLS) presenta una significancia estadística global y un alto poder explicativo, no es el modelo más idóneo para representar con precisión la complejidad del fenómeno económico de la publicidad política en plataformas digitales.
Aunque el modelo indica que el 84.3% de la variabilidad en las impresiones es explicada por el gasto y que ambos coeficientes de regresión son significativos, la validación de supuestos reveló fallas críticas. El incumplimiento de los supuestos de linealidad, normalidad y homocedasticidad invalida la fiabilidad de las inferencias estadísticas tradicionales en este contexto.
</div>
""", unsafe_allow_html=True)