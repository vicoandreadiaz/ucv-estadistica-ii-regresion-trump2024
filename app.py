import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Dashboard Trump 2024", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data/muestra_aleatoria_trump_2024.csv")

def descriptive_stats(series: pd.Series) -> dict:
    s = pd.to_numeric(series, errors="coerce").dropna()

    mode_series = s.mode()
    mode_value = mode_series.iloc[0] if not mode_series.empty else pd.NA

    return {
        "media": s.mean(),
        "mediana": s.median(),
        "moda": mode_value,
        "varianza": s.var(ddof=1),
        "desviacion_estandar": s.std(ddof=1),
        "min": s.min(),
        "max": s.max(),
        "n": int(s.shape[0]),
    }

df = load_data()

#Asegura numéricos
df["impresiones_superior"] = pd.to_numeric(df["impresiones_superior"], errors="coerce")
df["gasto_superior"] = pd.to_numeric(df["gasto_superior"], errors="coerce")

st.sidebar.header("Filtros")
#Límites reales de los datos (para validar entradas)
imp_min = int(df["impresiones_superior"].min())
imp_max = int(df["impresiones_superior"].max())
gas_min = float(df["gasto_superior"].min())
gas_max = float(df["gasto_superior"].max())
st.sidebar.caption(f"Impresiones permitidas: {imp_min:,} a {imp_max:,}")
st.sidebar.caption(f"Presupuesto permitido: {gas_min:,.2f} a {gas_max:,.2f}")

#Inputs de texto
imp_text = st.sidebar.text_input(
    "Máximo de impresiones",
    value=str(imp_max),
    help="Ingresa un número dentro del rango permitido."
)
gas_text = st.sidebar.text_input(
    "Máximo de gasto",
    value=f"{gas_max:.2f}",
    help="Ingresa un número dentro del rango permitido."
)

#Validación estricta: no menor al mínimo ni mayor al máximo
errores = []
# Impresiones (entero)
try:
    imp_top = int(imp_text.replace(",", "").strip())
    if imp_top < imp_min or imp_top > imp_max:
        errores.append(f"Máximo de impresiones fuera de rango ({imp_min} - {imp_max}).")
except Exception:
    errores.append("Máximo de impresiones debe ser un número entero válido.")
# Presupuesto (decimal)
try:
    gas_top = float(gas_text.replace(",", "").strip())
    if gas_top < gas_min or gas_top > gas_max:
        errores.append(f"Máximo de gasto fuera de rango ({gas_min:.2f} - {gas_max:.2f}).")
except Exception:
    errores.append("Máximo de gasto debe ser un número válido.")
if errores:
    for e in errores:
        st.sidebar.error(e)
    st.stop()

platform_options = sorted([p for p in df["plataforma"].dropna().unique()])
selected_platforms = st.sidebar.multiselect(
    "Plataforma",
    options=platform_options,
    default=platform_options,
)

#Aplicar filtros
if selected_platforms:
    df_f = df[df["plataforma"].astype(str).isin(selected_platforms)].copy()
else:
    df_f = df.iloc[0:0].copy()
df_f = df_f[
    (df_f["impresiones_superior"] <= imp_top) &
    (df_f["gasto_superior"] <= gas_top)
].copy()
st.title("Impresiones vs Presupuesto")
st.subheader("Gráfico de dispersión")

fig = px.scatter(
        df_f,
        x="gasto_superior",
        y="impresiones_superior",
        color="plataforma",
        opacity=0.75,
        title="Relación entre gasto e impresiones (por plataforma)",
        labels={
            "gasto_superior": "Presupuesto",
            "impresiones_superior": "Impresiones",
            "plataforma": "Plataforma",
        },
        template="plotly_white",
    )

# Margen del gráfico + estética
fig.update_layout(
        margin=dict(l=40, r=40, t=70, b=50),
        legend_title_text="Plataforma",
        title_x=0.02,
    )

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("Estadísticas descriptivas")
stats_df = pd.DataFrame({
        "Impresiones": descriptive_stats(df_f["impresiones_superior"]),
        "Presupuesto": descriptive_stats(df_f["gasto_superior"]),
    })

styled_stats = (
        stats_df.style
        .format("{:,.2f}", na_rep="-")
        .set_properties(**{
            "text-align": "center",
            "font-size": "14px"
        })
        .set_table_styles([
            {"selector": "th", "props": [("text-align", "center"), ("font-weight", "bold")]},
            {"selector": "td", "props": [("padding", "6px 10px")]},
        ])
    )
st.table(styled_stats)


st.caption(f"Registros filtrados: {len(df_f):,} | Registros graficados: {len(df_f):,}")


# CSS para personalizar estetica
st.markdown("""
<style>

    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #2c3e50 0%, #3498db 100%);
        color: white;
    }
    .css-1d391kg {
        background-color: #2c3e50;
    }
    /* Botones */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }
    /* Radio buttons */
    .stRadio > div {
        flex-direction: row;
        align-items: center;
        background-color: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .stRadio > label {
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #2c3e50;
    }
    /* Select boxes */
    .stMultiSelect [data-baseweb="select"] {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
    }
    .stMultiSelect [data-baseweb="select"]:hover {
        border-color: #667eea;
    }
    /* Separadores */
    .stMarkdown hr {
        margin: 3rem 0;
        border: none;
        height: 3px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
    }
    /* Dataframes */
    .dataframe {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    /* Colores coordinados para gráficos */
    .metric-card {
        background: linear-gradient(135deg, #f8f9ff 0%, #e8eeff 100%);
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
    }
    /* Sidebar con fondo oscuro */
    [data-testid="stSidebar"] {
        background-color: #2f2c79;
    }
        [data-testid="stSidebar"] * {
        color: white !important;
    }
    /* Labels y textos específicos del sidebar */
    [data-testid="stSidebar"] label {
        color: white !important;
        font-weight: 600;
    }
    [data-testid="stSidebar"] .stMultiSelect, 
    [data-testid="stSidebar"] .stSlider,  {
        color: white !important;
    }
        [data-testid="stSidebar"] .stDateInput input {
        color: black !important;
        background-color: white !important;
    }
    [data-testid="stSidebar"] .stDateInput label {
        color: white !important;
    }
            </style>
""", unsafe_allow_html=True)