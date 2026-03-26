import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# ==========================================
# 1. PREPARACIÓN DE DATOS Y MUESTREO PARA SPSS
# ==========================================
print("Cargando la matriz limpia...")
df_base_limpio = pd.read_csv(r'data/matriz_de_datos_trump_2024.csv')

# Muestreo Aleatorio Simple (1 muestra por ID de anuncio)
muestra_trump2024 = df_base_limpio.groupby('id_archivo_anuncio').sample(n=1, random_state=42)

# Exportación del DF que se usará en el software SPSS
muestra_trump2024.to_csv(r'data/muestra_aleatoria_trump_2024.csv', index=False)
print(f"Muestra para SPSS lista con {len(muestra_trump2024)} anuncios únicos.")


# ==========================================
# 2. PREPARACIÓN VISUAL Y CÁLCULO DE MUESTRAS (n)
# ==========================================
df_spss = muestra_trump2024.copy()

# Verificamos nulos
if df_spss['plataforma'].isnull().any():
    df_spss['plataforma'] = df_spss['plataforma'].fillna('Desconocida')

# Colores de campaña
paleta_campana = {
    'facebook': '#002868',   # Azul intenso
    'instagram': '#BF0A30',  # Rojo intenso
    'Desconocida': '#A9A9A9' # Gris
}

# Cálculos de los tamaños de muestra para los títulos de cada gráfico
n_total = len(df_spss)
n_zoom_10k = len(df_spss[(df_spss['gasto_superior'] <= 10000) & (df_spss['impresiones_superior'] <= 200000)])
n_zoom_2k  = len(df_spss[(df_spss['gasto_superior'] <= 2000) & (df_spss['impresiones_superior'] <= 50000)])


# ==========================================
# 3. GENERACIÓN DE GRÁFICOS
# ==========================================

# ---------------------------------------------------------
# GRÁFICO 1: VISTA GENERAL (TODOS LOS OUTLIERS)
# ---------------------------------------------------------
print("Generando Gráfico 1: Vista General...")
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df_spss, x='gasto_superior', y='impresiones_superior',
    hue='plataforma', palette=paleta_campana, alpha=0.7, edgecolor='white', s=80
)

plt.title(f'Correlación de Gasto vs. Impresiones\n(Vista General Trump 2024) | n={n_total}', 
          fontsize=14, fontweight='bold', color='#002868', pad=15)
plt.xlabel('Gasto Superior Estimado (USD)', fontsize=12, fontweight='bold', color='#BF0A30')
plt.ylabel('Impresiones Superiores Estimadas', fontsize=12, fontweight='bold', color='#BF0A30')

ax1 = plt.gca()
ax1.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{int(x):,}'))
ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, pos: f'{int(y):,}'))

plt.grid(True, linestyle='--', alpha=0.3, color='#A9A9A9')
plt.legend(title='Plataforma', title_fontsize='11', fontsize='10')
plt.tight_layout()

plt.savefig(r'data/dispersion_campana_trump.png', dpi=300)

# ---------------------------------------------------------
# GRÁFICO 2: ZOOM (Gasto < $10k e Impresiones < 200k)
# ---------------------------------------------------------
print("Generando Gráfico 2: Zoom 10k...")
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df_spss, x='gasto_superior', y='impresiones_superior',
    hue='plataforma', palette=paleta_campana, alpha=0.7, edgecolor='white', s=80
)

plt.xlim(0, 10000)
plt.ylim(0, 200000)

plt.title(f'Correlación de Gasto vs. Impresiones\n(Zoom: Gasto < $10k e Impresiones < 200k) | n={n_zoom_10k}', 
          fontsize=14, fontweight='bold', color='#002868', pad=15)
plt.xlabel('Gasto Superior Estimado (USD)', fontsize=12, fontweight='bold', color='#BF0A30')
plt.ylabel('Impresiones Superiores Estimadas', fontsize=12, fontweight='bold', color='#BF0A30')

ax2 = plt.gca()
ax2.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{int(x):,}'))
ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, pos: f'{int(y):,}'))

plt.grid(True, linestyle='--', alpha=0.3, color='#A9A9A9')
plt.legend(title='Plataforma', title_fontsize='11', fontsize='10')
plt.tight_layout()

plt.savefig(r'data/dispersion_zoom_trump.png', dpi=300)

# ---------------------------------------------------------
# GRÁFICO 3: SÚPER ZOOM (Gasto < $2k e Impresiones < 50k)
# ---------------------------------------------------------
print("Generando Gráfico 3: Súper Zoom 2k...")
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df_spss, x='gasto_superior', y='impresiones_superior',
    hue='plataforma', palette=paleta_campana, alpha=0.7, edgecolor='white', s=80
)

plt.xlim(0, 2000)
plt.ylim(0, 50000)

plt.title(f'Correlación de Gasto vs. Impresiones\n(Súper Zoom: Gasto < $2k e Impresiones < 50k) | n={n_zoom_2k}', 
          fontsize=14, fontweight='bold', color='#002868', pad=15)
plt.xlabel('Gasto Superior Estimado (USD)', fontsize=12, fontweight='bold', color='#BF0A30')
plt.ylabel('Impresiones Superiores Estimadas', fontsize=12, fontweight='bold', color='#BF0A30')

ax3 = plt.gca()
ax3.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{int(x):,}'))
ax3.yaxis.set_major_formatter(FuncFormatter(lambda y, pos: f'{int(y):,}'))

plt.grid(True, linestyle='--', alpha=0.3, color='#A9A9A9')
plt.legend(title='Plataforma', title_fontsize='11', fontsize='10')
plt.tight_layout()

plt.savefig(r'data/dispersion_super_zoom_trump.png', dpi=300)

print("\n¡Proceso finalizado con éxito! Revisa tu carpeta 'data' para ver las 3 imágenes y el CSV para SPSS.")