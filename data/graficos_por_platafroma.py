import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# ==========================================
# 1. IMPORTAR VARIABLES DEL MÓDULO ANTERIOR
# ==========================================
# Aquí es donde ocurre la magia: traemos los datos y colores desde muestra.py
from muestra import df_spss, paleta_campana

print("\nIniciando módulo de gráficos individuales por plataforma...")

# Nos aseguramos de que el texto de plataforma esté en minúsculas para que los filtros no fallen
df_spss['plataforma'] = df_spss['plataforma'].astype(str).str.lower().str.strip()

plataformas_a_analizar = ['facebook', 'instagram']

# ==========================================
# 2. FUNCIÓN GENERADORA DE GRÁFICOS
# ==========================================
def crear_y_guardar_grafico(df_datos, color_puntos, titulo, nombre_archivo, limite_x=None, limite_y=None):
    plt.figure(figsize=(10, 6))
    
    sns.scatterplot(
        data=df_datos, x='gasto_superior', y='impresiones_superior',
        color=color_puntos, alpha=0.7, edgecolor='white', s=80
    )
    
    # Aplicar Zoom si indicamos los límites
    if limite_x is not None and limite_y is not None:
        plt.xlim(0, limite_x)
        plt.ylim(0, limite_y)
        
    plt.title(titulo, fontsize=14, fontweight='bold', color=color_puntos, pad=15)
    plt.xlabel('Gasto Superior Estimado (USD)', fontsize=12, fontweight='bold', color='black')
    plt.ylabel('Impresiones Superiores Estimadas', fontsize=12, fontweight='bold', color='black')
    
    ax = plt.gca()
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{int(x):,}'))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, pos: f'{int(y):,}'))
    
    plt.grid(True, linestyle='--', alpha=0.3, color='#A9A9A9')
    plt.tight_layout()
    
    ruta = rf"data/{nombre_archivo}"
    plt.savefig(ruta, dpi=300)
    plt.close() # Cierra la figura para ahorrar memoria
    print(f"  -> Guardado: {nombre_archivo}")

# ==========================================
# 3. BUCLE POR PLATAFORMA
# ==========================================
for plat in plataformas_a_analizar:
    print(f"\n--- Procesando: {plat.upper()} ---")
    
    # Filtrar datos de la plataforma específica
    df_plat = df_spss[df_spss['plataforma'] == plat]
    
    if df_plat.empty:
        print(f"  Aviso: No hay datos para {plat}.")
        continue
        
    color_plat = paleta_campana.get(plat, '#A9A9A9')
    
    # Calcular los tamaños de la muestra (n) para esta plataforma específica
    n_total = len(df_plat)
    n_zoom_10k = len(df_plat[(df_plat['gasto_superior'] <= 10000) & (df_plat['impresiones_superior'] <= 200000)])
    n_zoom_2k  = len(df_plat[(df_plat['gasto_superior'] <= 2000) & (df_plat['impresiones_superior'] <= 50000)])
    
    # Generar los 3 gráficos con su respectiva 'n'
    titulo_gen = f'{plat.capitalize()}: Gasto vs. Impresiones (General) | n={n_total}'
    crear_y_guardar_grafico(df_plat, color_plat, titulo_gen, f'dispersion_{plat}_1_general.png')
    
    titulo_10k = f'{plat.capitalize()}: Gasto vs. Impresiones (Zoom < $10k, < 200k) | n={n_zoom_10k}'
    crear_y_guardar_grafico(df_plat, color_plat, titulo_10k, f'dispersion_{plat}_2_zoom_10k.png', 10000, 200000)
    
    titulo_2k = f'{plat.capitalize()}: Gasto vs. Impresiones (Súper Zoom < $2k, < 50k) | n={n_zoom_2k}'
    crear_y_guardar_grafico(df_plat, color_plat, titulo_2k, f'dispersion_{plat}_3_zoom_2k.png', 2000, 50000)

print("\n¡Gráficos individuales por plataforma creados con éxito!")