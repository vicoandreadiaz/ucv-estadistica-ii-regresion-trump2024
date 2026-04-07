import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Análisis Preliminar - Trump 2024", page_icon="📊", layout="wide")

# --- 2. CARGA DE DATOS ---
@st.cache_data
def load_data():
    path = "muestra_aleatoria_trump_2024.csv" # Buscamos en la raíz
    if not os.path.exists(path):
        path = "data/muestra_aleatoria_trump_2024.csv" # O en la carpeta data
        
    if os.path.exists(path):
        df = pd.read_csv(path)
        # LIMPIEZA CRÍTICA: Quitar espacios invisibles en los nombres de las columnas
        df.columns = df.columns.str.strip()
        
        # Convertir a numérico asegurando que no haya errores
        df["impresiones_superior"] = pd.to_numeric(df["impresiones_superior"], errors="coerce")
        df["gasto_superior"] = pd.to_numeric(df["gasto_superior"], errors="coerce")
        
        return df.dropna(subset=["impresiones_superior", "gasto_superior"])
    return pd.DataFrame()

def get_stats(series):
    return {
        "Media": series.mean(),
        "Mediana": series.median(),
        "Moda": series.mode().iloc[0] if not series.mode().empty else 0,
        "Varianza": series.var(),
        "Desv. Est.": series.std(),
        "Mínimo": series.min(),
        "Máximo": series.max()
    }

# --- 3. ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp { background-color: white; }
    [data-testid="stSidebar"] { background-color: #003366; }
    [data-testid="stSidebar"] * { color: white !important; }
    .metric-card {
        background-color: #f8f9fa;
        border-top: 4px solid #FFCC00;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .metric-value { font-size: 1.1rem; font-weight: bold; color: #003366; }
    .metric-label { font-size: 0.7rem; color: #666; text-transform: uppercase; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

df = load_data()

if df.empty:
    st.error("⚠️ No se encontró el archivo 'muestra_aleatoria_trump_2024.csv'. Asegúrate de que el nombre sea exacto.")
    st.stop()

# --- 4. SIDEBAR (FILTROS) ---
st.sidebar.header("⚙️ Filtros de la Muestra")

# Límites dinámicos
imp_max_val = int(df["impresiones_superior"].max())
gas_max_val = float(df["gasto_superior"].max())

max_imp = st.sidebar.number_input("Impresiones máximas:", 0, imp_max_val, imp_max_val)
max_gas = st.sidebar.number_input("Gasto máximo (USD):", 0.0, gas_max_val, gas_max_val)

# Filtro de plataforma (si existe la columna)
if 'plataforma' in df.columns:
    opciones_plat = df['plataforma'].unique()
    plats = st.sidebar.multiselect("Plataformas:", opciones_plat, default=opciones_plat)
    df_f = df[
        (df["impresiones_superior"] <= max_imp) & 
        (df["gasto_superior"] <= max_gas) & 
        (df["plataforma"].isin(plats))
    ]
else:
    df_f = df[(df["impresiones_superior"] <= max_imp) & (df["gasto_superior"] <= max_gas)]

# --- 5. TÍTULO Y GRÁFICO ---
st.markdown("<h1 style='text-align: center; color: #003366;'>📊 Análisis Preliminar de Datos</h1>", unsafe_allow_html=True)

fig = px.scatter(
    df_f, x="gasto_superior", y="impresiones_superior",
    color="plataforma" if 'plataforma' in df.columns else None,
    title="Relación Gasto vs. Impresiones",
    labels={"gasto_superior": "Gasto (USD)", "impresiones_superior": "Impresiones"},
    template="plotly_white",
    opacity=0.6,
    color_discrete_map={"facebook": "#1877F2", "instagram": "#E4405F", "facebook_instagram": "#833AB4"}
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- 6. ESTADÍSTICAS DESCRIPTIVAS EN COLUMNAS ---
st.subheader("📐 Estadísticas Descriptivas")

def render_metric_row(label_title, data_series, is_currency=False):
    st.markdown(f"**{label_title}**")
    stats = get_stats(data_series)
    cols = st.columns(7)
    metrics_list = ["Media", "Mediana", "Moda", "Varianza", "Desv. Est.", "Mínimo", "Máximo"]
    
    for i, m in enumerate(metrics_list):
        val = stats[m]
        # Formato de moneda o número entero
        if is_currency:
            formatted_val = f"${val:,.2f}"
        else:
            formatted_val = f"{val:,.0f}"
            
        with cols[i]:
            st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">{m}</div>
                    <div class="metric-value">{formatted_val}</div>
                </div>
            """, unsafe_allow_html=True)
    st.write("")

render_metric_row("Variable Dependiente (Y): Impresiones", df_f["impresiones_superior"])
render_metric_row("Variable Independiente (X): Gasto", df_f["gasto_superior"], is_currency=True)

st.caption(f"Mostrando {len(df_f):,} anuncios de una muestra total de {len(df):,}.")