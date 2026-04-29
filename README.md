# El Modelo de Regresión Lineal Simple como predictor del costo de la Visibilidad en Publicidad Política Digital

**Un estudio acerca del ajuste y la idoneidad del modelo para explicar el costo de la visibilidad publicitaria de Donald Trump en las Elecciones de 2024.**

---

**Universidad Central de Venezuela** Facultad de Ciencias Económicas y Sociales  
Escuela de Estadística y Ciencias Actuariales  
Cátedra: Estadística II  

**Integrantes:** Victoria Díaz, Vicente Díaz  
**Docentes Asesores:** Prof. Sandra Pinto, Prof. Yuraisi Capriles  

---

## 🔗 Acceso al Dashboard Interactivo
El despliegue interactivo de los resultados, los estadísticos y el simulador de predicción se encuentra disponible públicamente en el siguiente enlace:  
[https://trump-mrls-2024.streamlit.app/](https://trump-mrls-2024.streamlit.app/)

---

## 📝 Resumen de la Investigación
El presente repositorio aloja el código fuente y el entorno de presentación interactiva correspondiente al trabajo final de investigación. El estudio tiene como propósito central analizar el ajuste y la idoneidad del Modelo de Regresión Lineal Simple (MRLS) como herramienta predictiva para estimar el costo de la visibilidad publicitaria en el ecosistema digital.

A través de un diseño metodológico estructurado y el procesamiento de una muestra extraída de la *Meta Ads Library*, se evaluó la relación funcional bivariante entre el gasto publicitario estimado (Variable Independiente) y las impresiones máximas generadas (Variable Dependiente) por la campaña presidencial de Donald J. Trump en 2024.

## 📊 Hallazgos y Conclusiones Principales
Con base en el desarrollo empírico y la evaluación de los supuestos, la investigación concluye lo siguiente:

1. **Aproximación de Tendencia:** El MRLS funciona como una aproximación inicial útil para identificar una tendencia general, logrando explicar una alta proporción de la variabilidad de las impresiones a través del Coeficiente de Determinación ($R^2$).
2. **Incumplimiento de Supuestos:** Las variables en estudio confirman que el gasto y las impresiones en publicidad política digital no siguen una distribución normal y presentan problemas de heterocedasticidad. Están influenciadas por factores externos (como segmentación geográfica, demográfica y el sistema de subastas del algoritmo) que el modelo bivariante actual deja fuera.
3. **Idoneidad Estructural:** Dada la naturaleza dinámica y estocástica de la publicidad en redes sociales, se determina que el MRLS resulta insuficiente y no es estructuralmente idóneo como predictor único. Esta realidad exige el uso de modelos econométricos multivariantes o estocásticos más avanzados para obtener proyecciones rigurosas y profesionalmente válidas.

## 🗂️ Estructura del Aplicativo Web
La arquitectura de la aplicación en Streamlit respeta las fases de la investigación documental:
* **Planteamiento y Marco Teórico:** Fundamentación del ecosistema de Meta y teoría estadística bivariante.
* **Marco Metodológico:** Tratamiento del universo de datos y delimitación de la muestra aleatoria ($n=2000$).
* **Desarrollo Empírico Preliminar:** Tratamiento computacional de los datos mediante Python (Pandas) y gráficos de dispersión interactivos (Plotly).
* **Resultados Inferenciales y Simulador:** Exposición de los *outputs* de IBM SPSS Statistics (Correlación, ANOVA, Coeficientes), evaluación crítica de residuos e implementación de una calculadora de estimación iterativa.

## 💻 Tecnologías Implementadas
* **Procesamiento Estadístico Inferencial:** IBM SPSS Statistics
* **Lenguaje y Entorno Web:** Python 3 (Streamlit, Pandas, Plotly Graph Objects)
* **Notación Matemática:** LaTeX

---

## 🎓 Agradecimientos Especiales
Extendemos nuestro más sincero agradecimiento a la **Prof. Sandra Pinto** y a la **Prof. Yuraisi Capriles**. Gracias por brindarnos sus invaluables luces, por su vocación docente y por la guía metodológica a lo largo de toda la materia. Su dedicación fue un pilar fundamental para la culminación exitosa de este proyecto de investigación.

---
*Caracas, Venezuela - 2024*
