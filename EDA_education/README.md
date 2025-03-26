# Análisis Exploratorio de Datos: Influencia del Nivel Económico sobre la Educación en Madrid

## Tabla de contenidos:

1. [Descripción](#descripción)
2. [Datos](#datos)
3. [Resultados](#resultados)
4. [Contacto](#contacto)
5. [Agradecimientos](#agradecimientos)

## Descripción

Este proyecto realiza un Análisis Exploratorio de Datos (EDA) para investigar cómo el nivel económico de las familias afecta la educación de sus hijos en Madrid. Usando datos obtenidos del Ayuntamiento de Madrid, se examinan diversas métricas educativas y económicas para identificar patrones y relaciones significativas. Para poder realizar con más detalle este análisis he selecccionado el año 2014 (pre-pandemia) y el año 2020 (medidas optadas excepcionalmente por la situación de pandemia mundial)

## Datos

Los datos utilizados en este análisis provienen de:

- **Renta media anual por hogar**: Contiene información sobre los ingresos medios anuales de las familias en los diferentes distritos de Madrid. Estos datos han sido recopilados del [Portal de datos abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/)
- **Resultados académicos**: Incluye estadísticas sobre el rendimiento académico de los estudiantes en los niveles de enseñanza obligatoria (Primaria y Secundaria). Para la recopilación de esta información he investigado en la página web de [Estadística de la Enseñanza de la Comunidad de Madrid](https://estadisticas.educa.madrid.org/)

### Diccionario de Datos

|Variable|Descripción|
|-|-|
|`Niveles`|Etapa educativa obligatoria (Primaria y ESO)|
|`Total`|Total de alumnos matricualados en cada nivel|
|`Distrito`|Distrito de Madrid al que pertenecen los datos|
|`Curso_escolar`|Cursos de los años que representan los datos|
|`Tasa_idoneidad_%`|Tasa de efectividad del nivel educativo. El número reflejado corresponde a las personas que sí han superado ese nivel con respecto al total de matriculados (En porcentaje)|
|`Renta`|Renta media anual de los hogares de cada distrito y de cada año|
|`Año`|Año que corresponde a la renta media anual|

## Resultados

En esta sección se presentan los principales hallazgos del análisis:

- **Correlación Renta-Tasa de idoneidad**: Se observó una correlación positiva moderada entre la renta media anual de las familias y la tasa de idoneidad de los diferentes niveles educativos analizados. Por lo tanto, a medida que aumenta la renta, también tiende a aumentar la tasa de idoneidad.
- **Disparidades Geográficas**: Zonas con rentas anuales significativamente menores que en otras zonas presentan una tasa de idoneidad baja.
- **Otros Factores**: Además de la renta, influyen otros factores como la calidad de la educación, las infraestructuras, las políticas educativas...

Puedes explorar los resultados completos en el [notebook del análisis](./main.ipynb).

## Contacto

Para cualquier pregunta o comentario, puedes contactarme a través de:

- Correo electrónico: somm14DS@gmail.com
- LinkedIn: linkedin.com/in/sorayamm

## Agradecimientos

Agradecimientos especiales a:

- El Ayuntamiento de Madrid por proporcionar los datos necesarios para este análisis.
- Profesores y compañeros de los cursos de análisis de datos por sus valiosos comentarios y sugerencias.
