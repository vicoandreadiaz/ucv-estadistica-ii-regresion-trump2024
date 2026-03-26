import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt

# ==========================================
# 1. CARGAR DATOS Y CALCULAR EL MODELO
# ==========================================
print("Calculando estadísticas para la tabla...")
df_modelo = pd.read_csv(r'data/muestra_aleatoria_trump_2024.csv')
modelo = ols('impresiones_superior ~ gasto_superior', data=df_modelo).fit()
tabla_anova = sm.stats.anova_lm(modelo, typ=1)

# ==========================================
# 2. PREPARAR LOS DATOS PARA LA TABLA VISUAL
# ==========================================
# Creamos una lista de listas. La primera fila son los encabezados.
# Formateamos los números grandes con notación científica (.2e) o decimales (.2f)
datos_tabla = [
    ["Métrica Estadística", "Valor Calculado", "Interpretación para el Estudio"],
    ["R-cuadrado (R²)", f"{modelo.rsquared:.4f}", "El 84.3% de las impresiones se explica por el gasto."],
    ["Estadístico F (ANOVA)", f"{modelo.fvalue:,.2f}", "El modelo es globalmente significativo."],
    ["Valor p (ANOVA)", "< 0.001", "Se rechaza la hipótesis nula (p < 0.05)."],
    ["Coeficiente (Gasto)", f"{modelo.params['gasto_superior']:.2f}", "Por cada $1 USD, se obtienen ~26 impresiones."],
    ["Intercepto", f"{modelo.params['Intercept']:.2f}", "Valor base teórico del modelo."]
]

# ==========================================
# 3. DIBUJAR LA TABLA ESTÉTICA
# ==========================================
print("Generando imagen de la tabla...")

# Creamos un lienzo ancho pero bajito (10 pulgadas de ancho por 3 de alto)
fig, ax = plt.subplots(figsize=(10, 3.5))

# Ocultamos los ejes gráficos (las líneas X e Y) porque solo queremos la tabla
ax.axis('tight')
ax.axis('off')

# Dibujamos la tabla usando los datos que preparamos arriba
tabla = ax.table(cellText=datos_tabla, loc='center', cellLoc='center')

# Ajustamos el tamaño de la letra y el alto de las celdas
tabla.auto_set_font_size(False)
tabla.set_fontsize(11)
tabla.scale(1, 1.8) # Escala el ancho (1x) y el alto de las filas (1.8x)

# ==========================================
# 4. APLICAR COLORES (DISEÑO ESTÉTICO)
# ==========================================
# Recorremos cada celda de la tabla para pintarla
for (fila, columna), celda in tabla.get_celld().items():
    # Si es la fila 0 (Los encabezados)
    if fila == 0:
        celda.set_text_props(weight='bold', color='white') # Texto blanco y negrita
        celda.set_facecolor('#002868') # Fondo Azul Intenso de la campaña
    # Si son las filas de datos
    else:
        celda.set_facecolor('#f9f9f9') # Un gris súper claro para el fondo
        
        # Ponemos en negrita la primera columna (los nombres de las métricas)
        if columna == 0:
            celda.set_text_props(weight='bold')

# Añadimos un título principal encima de la tabla
plt.title("Resumen Estadístico: Análisis de Varianza (ANOVA) y Regresión", 
          fontweight='bold', color='#BF0A30', pad=20, fontsize=14) # Rojo Intenso

# ==========================================
# 5. GUARDAR LA IMAGEN
# ==========================================
plt.tight_layout()
ruta_imagen = r'data/tabla_resultados_esteticos.png'
plt.savefig(ruta_imagen, dpi=300, bbox_inches='tight') # bbox_inches recorta los bordes blancos extra

print(f"¡Éxito! Tu tabla estética se guardó en: {ruta_imagen}")