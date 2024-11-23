# Predicción del Rendimiento Estudiantil en Estudios Avanzados🎓
Este proyecto utiliza **Machine Learning** para predecir el rendimiento y la retención de estudiantes en educación superior, basado en datos del dataset [Higher Education Predictors of Student Retention](https://www.kaggle.com/datasets/thedevastator/higher-education-predictors-of-student-retention). El objetivo principal es *identificar patrones que influyen en el éxito estudiantil y mejorar estrategias de intervención académica*.

## Tabla de contenidos:
1. [Descripción del problema](#descripción-del-problema)
2. [Acerca del Dataset](#acerca-del-dataset)
3. [Metodología](#metodología)
4. [Resultados](#resultados)
5. [Contacto](#contacto)
6. [Agradecimientos](#agradecimientos)

## Descripción del problema
La deserción estudiantil es un desafío clave para las instituciones de educación superior. Este proyecto busca responder a preguntas como:
- ¿Qué factores son más influyentes en el rendimiento estudiantil?
- ¿Es posible predecir con precisión el éxito de los estudiantes en función de su historial académico y características personales?

El enfoque principal es *desarrollar modelos predictivos que puedan ayudar a identificar estudiantes en riesgo*.

## Acerca del Dataset
El dataset incluye diversas características relacionadas con los estudiantes, como:
- Datos demográficos: estado civil, nacionalidad...
- Datos socioeconómicos: Estudios y ocupación de los padres, beca, deudor...
- Datos macroeconómicos: Tasa de desempleo, infación, PIB...
- Datos académicos: Curso, estudios previos, asistencia, unidades por semestre...
  
Más detalles están disponibles en el [dataset original](https://www.kaggle.com/datasets/thedevastator/higher-education-predictors-of-student-retention).

## Metodología
El proyecto se desarrolló en los siguientes pasos:
1. **Preprocesamiento de datos**:
   - Transformaciones iniciales para comprender valores numéricos que correspoden categorías en formato de texto.
   - Fuente de información: [Repositorio en GitHub](https://github.com/carmelh/SQL_projects/tree/main/student_data_analysis/Datasets)
2. **Análisis Exploratorio de Datos (EDA)**:
    - Análisis de correlaciones y tendencias claves con diversas ténicas de selección.
3. **Pipelines**:
    - Preprocesamiento de datos.
4. **Selección de modelos**:
   - Evaluación inicial de varios algoritmos de Machine Learning mediante **Cross Validation** incluyendo:
       - Random Forest.
       - XGBoost.
       - LightGBM.
       - CatBoost
5. **Optimización**
   - Uso de **GridSearchCV** para optimizar hiperparámetros.
   - Técnica **SMOTE** de la librería *Imbalanced-learn*.
6. **Evaluación**:
   - Métricas de rendimiento: `precision`, `recall` y `F1-score`

## Resultados
Los modelos lograron predecir el rendimiento estudiantil con los siguientes resultados destacados:
- **Modelo seleccionado**: XGBoost con la técnica `SMOTE`.
- **Rendimiento en conjunto de *Test***:
    - `Precision`: (**Dropout**: 91%) - (**Graduate**:93%)
    - `Recall`: (**Dropout**: 89%) - (**Graduate**:95%)
    - `F1-score`: (**Dropout**: 90%) - (**Graduate**:94%)
- **Factores más relevantes**:
    - Después de hacer diferentes análisis para seleccionar las *Features* y de la selección del modelo, la mejor métrica conseguida fue abarcando todas las variables.

Más detalles sobre los resultados están disponibles en la ['memoria'](./memoria.ipynb) del proyecto.

## Contacto
Para cualquier pregunta o comentario, puedes contactarme a través de:
- Correo electrónico: somm14DS@gmail.com
- LinkedIn: https://www.linkedin.com/in/sorayamm/

## Agradecimientos
Agradecimientos especiales a:
- A la plataforma [Kaggle](https://www.kaggle.com/datasets) por proporcionar de manera pública los datos utilizados para realizar este proyecto.
- Profesores y compañeros de los cursos de análisis de datos por su ayuda y sugerencias.
