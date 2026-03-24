import pandas as pd
import json
import re

def generar_matriz_unica(ruta_csv):
    """
    Lee un CSV de anuncios extraídos de Meta Ads Libray, traduce al español, extrae los límites de 
    gasto e impresiones en columnas separadas, y aplana todas las listas 
    anidadas para generar una matriz de datos única.
    """
    df = pd.read_csv(ruta_csv)
    
    # 1. Lo primero que hacemos es renombrar las columnas directas al español
    renombrar_cols = {
        'ad_archive_id': 'id_archivo_anuncio',
        'page_id': 'id_pagina',
        'page_name': 'nombre_pagina',
        'ad_creation_time': 'fecha_creacion_anuncio',
        'ad_delivery_start_time': 'fecha_inicio_entrega',
        'ad_delivery_stop_time': 'fecha_fin_entrega',
        'byline': 'autor_patrocinador',
        'ad_creative_bodies': 'cuerpos_creativos_anuncio',
        'ad_creative_link_titles': 'titulos_enlaces_creativos',
        'ad_creative_link_captions': 'leyendas_enlaces_creativos',
        'ad_creative_link_descriptions': 'descripciones_enlaces_creativos',
        'currency': 'moneda',
        'estimated_audience_size': 'tamano_audiencia_estimada',
        'languages': 'idiomas'
    }
    df = df.rename(columns=renombrar_cols)
    
    # 2. Luego, extraemos los límites del gasto e impresiones, que son las variables de interés.
    def extraer_limites(texto):
        if pd.isna(texto):
            return None, None
        texto = str(texto)
        # Buscar ambos límites usando expresiones regulares
        match = re.search(r'lower_bound:\s*(\d+).*?upper_bound:\s*(\d+)', texto)
        if match:
            return int(match.group(1)), int(match.group(2))
        
        # En caso de que aparezca un solo número directo por alguna anomalía en los datos
        match_single = re.search(r'\d+', texto)
        if match_single:
            val = int(match_single.group())
            return val, val
        return None, None

    # 3. Aplicamos la extracción a impresiones y gasto creando columnas nuevas. 
    # La función 'zip' nos permite recibir los 2 valores y ponerlos en 2 columnas al mismo tiempo
    df['impresiones_inferior'], df['impresiones_superior'] = zip(*df['impressions'].apply(extraer_limites))
    df['gasto_inferior'], df['gasto_superior'] = zip(*df['spend'].apply(extraer_limites))
    
    # Descartamos las columnas originales en inglés que unían este texto para trabajar con las creadas en el paso 4
    df = df.drop(columns=['impressions', 'spend'])
    
    # 4. Función auxiliar para leer los JSON anidados
    def parse_json_array(texto):
        if pd.isna(texto):
            return []
        texto = str(texto).strip()
        try:
            if texto.startswith('{') and texto.endswith('}'):
                return json.loads('[' + texto + ']')
            elif texto.startswith('[') and texto.endswith(']'):
                return json.loads(texto)
            return []
        except:
            return []
            
    # 5. Preparar los datos anidados
    df['plataforma_temp'] = df['publisher_platforms'].apply(lambda x: str(x).split(',') if pd.notna(x) else [])
    df['demografia_temp'] = df['demographic_distribution'].apply(parse_json_array)
    df['region_temp'] = df['delivery_by_region'].apply(parse_json_array)
    
    df['plataforma_temp'] = df['plataforma_temp'].apply(lambda x: x if len(x) > 0 else [None])
    df['demografia_temp'] = df['demografia_temp'].apply(lambda x: x if len(x) > 0 else [{}])
    df['region_temp'] = df['region_temp'].apply(lambda x: x if len(x) > 0 else [{}])
    
    # 6. Atomizamos cada uno de los datos de la matriz
    df_plano = df.explode('plataforma_temp').explode('demografia_temp').explode('region_temp')
    
    # 7. Extraer valores finales a las columnas
    df_plano['plataforma'] = df_plano['plataforma_temp']
    
    df_plano['demografia_edad'] = df_plano['demografia_temp'].apply(lambda x: x.get('age') if isinstance(x, dict) else None)
    df_plano['demografia_genero'] = df_plano['demografia_temp'].apply(lambda x: x.get('gender') if isinstance(x, dict) else None)
    df_plano['demografia_porcentaje'] = df_plano['demografia_temp'].apply(lambda x: x.get('percentage') if isinstance(x, dict) else None)
    
    df_plano['region_nombre'] = df_plano['region_temp'].apply(lambda x: x.get('region') if isinstance(x, dict) else None)
    df_plano['region_porcentaje'] = df_plano['region_temp'].apply(lambda x: x.get('percentage') if isinstance(x, dict) else None)
    
    # Limpiar columnas residuales
    df_plano = df_plano.drop(columns=[
        'plataforma_temp', 'demografia_temp', 'region_temp',
        'demographic_distribution', 'delivery_by_region', 'publisher_platforms'
    ])
    
    return df_plano
 
# 1. Llamar a la función
df_final = generar_matriz_unica('data_base/2026.csv')

# 2. Exportar el CSV de resultados
df_final.to_csv('data_base/matriz_de_datos_trump_2024.csv', index=False)