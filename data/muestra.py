import pandas as pd
# PREPARACIÓN DE DATOS PARA LA VERIFICACIÓN DE SUPUESTOS

# 1. Cargar la matriz limpia que generaste con limpieza.py
df_base_limpio = pd.read_csv(r'data/matriz_de_datos_trump_2024.csv')

# 2. Muestreo Aleatorio Simple (1 muestra por ID de anuncio)
muestra_trump2024 = df_base_limpio.groupby('id_archivo_anuncio').sample(n=1, random_state=42)

# 3. Comprobación
print(f"Total de registros originales: {len(df_base_limpio)}")
print(f"Total de registros para el modelo (únicos): {len(muestra_trump2024)}")

# 4. Exportación del DF que se usará en el software SPSS

muestra_trump2024.to_csv(r'data/muestra_aleatoria_trump_2024.csv', index=False)