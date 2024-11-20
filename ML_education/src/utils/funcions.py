import os
os.chdir('..') # Modifico a una carpeta hacia atras
from utils.modulos import *


def listado_categorias(df_categorizacion, lista_tipo = []):
    '''
    Instanciación de diccionarios para cada una de los tipos de categorización de las variables de un DataFrame (DF).

    Argumentos:
    df_categorización (pd.DataFrame): DF donde aparece la información de la categorización de cada variable el cual tiene columnas llamadas 'nombre_variable' y 'tipo_sugerido'. La primera hace referencia al nombre de la variable y la segunda al tipo de categorización.
    list_tipo (list[str]): Lista de nombres del tipo de categorización que quiero crear como diccionario.

    Retorna:
    resultado(dict): Crea listas de variables según el tipo de categorización dada.
    '''
    resultado = {}
    for t in lista_tipo:
        lista_var = [var for var,cat in zip(df_categorizacion['nombre_variable'], df_categorizacion['tipo_sugerido']) if cat == t]
        resultado[t] = lista_var
    return resultado


def generar_mapeos(directorio, correspondencia):
    '''
    Con esta función genera los mapeos de las variables categóricas codificadas.

    Argumentos:
    directorio(str): Ruta de la ruta dónde se encuentran los ficheros.
    correpondencia(dict): Diccionario donde incluye como clave el nombre del archivo y las columnas a la que corresponde su codificación 

    Retorna:
    resultados(dict): Diccionario donde se encuentra como clave el nombre de la variable dada. Como valor son los nombres correspondientes a cada dato numérico.
    '''
    resultados = {} # Creo diccionario para almacenar toda la información
    for file in os.listdir(directorio): # Itero entre la lista de variables y los ficheros a la vez
        nombre_archivo = re.sub(r'^.*?_(.*?)\.csv$', r'\1',file) # Me quedo exclusivamente con el nombre "limpio" del archivo
        if nombre_archivo in correspondencia: # Itero sobre las claves de los nombres de los archivos que contienen el nombre de las columnas del DF
            if nombre_archivo == 'parent_occupation' or nombre_archivo == 'parent_previous_quals': # Es el único que tiene que mapear varias columnas 
                nombre_col = correspondencia[nombre_archivo] 
                cat_df = pd.read_csv(os.path.join(directorio,file)) # Creo el DF
                cat_df.dropna(axis=0, inplace=True) # Elimino los nulos que se genera
                # Como cada df tiene nombres de columnas diferentes, instancio por su localizacion
                ID = cat_df.iloc[:,0] 
                values = cat_df.iloc[:,1]
                # Creo diccionario para almacenar los numeros y sus correspondientes valores
                file_data = dict(zip(ID,values))
                for columna in nombre_col: # Itero en la lista de la columnas originales
                    resultados[columna] = file_data # Lo almaceno en el diccionario con el nombre de la columna original
            else: # Si no es, hago lo mismo pero sin iterar dentro de la clave ya que solo hay un único valor
                nombre_col = correspondencia[nombre_archivo]
                cat_df = pd.read_csv(os.path.join(directorio,file))
                cat_df.dropna(axis=0, inplace=True) 
                ID = cat_df.iloc[:,0] 
                values = cat_df.iloc[:,1]
                file_data = dict(zip(ID,values))
                resultados[nombre_col] = file_data
            
    return resultados

def mapear(df_original, directorio, correspondencia):
    '''
    Con esta función se mapea los datos del DF con ayuda de la función anterior insertándola de manera recursiva.

    Argumentos:
    df(pd.DataFrame): DF original del cual quiero mapear.
    directorio(str): Ruta de la ruta dónde se encuentran los ficheros.
    correpondencia(dict): Diccionario donde incluye como clave el nombre del archivo y las columnas a la que corresponde su codificación.

    Retorna:
    df(pd.DataFrame): DF mapeado

    '''
    df_mapeo = df_original.copy() # Hago una copia porque sino se sobreescribe en el df orginal
    mapeo_categorico = generar_mapeos(directorio, correspondencia) # Función recursiva
    for col, mapeo in mapeo_categorico.items(): # Itero sobre mi mapeo
        if col in df_mapeo.columns: # Si existen en el DF original
            df_mapeo[col] = df_mapeo[col].map(mapeo) # Mapeo
    return df_mapeo


def mapear_ordinal(df_original, mapeo_num, columna):
    '''
    Función para mapear de manera ordinal las variables codificadas pero que sí tienen un sentido.

    Argumentos:
    df(pd.DataFrame): DF original del cual quiero mapear.
    mapeo_num(dict): Diccionario donde la clave representa el valor que viene predeterminado en el DF original y el valor al número que quiero transformar.
    columna(str): Nombre de la columna que quiero mapear

    Retorna:
    df(pd.DataFrame): DF mapeado
    '''
    df_mapeo = df_original.copy()
    if isinstance(columna, list):
        for col in columna:
            df_mapeo[col] = df_mapeo[col].map(mapeo_num)
    else:
        df_mapeo[columna] = df_mapeo[columna].map(mapeo_num)
    return df_mapeo


def mutual_information(train, lista_cat, target_col):
    '''
    Analiza el test Mutual Information

    Argumentos:
    train(pd.DataFrame): Set de entrenamiento.
    lista_cat(list): Lista de todas las variables categóricas.
    target_col(str): Variable objetivo

    Retorna:
    mi(dict): Diccionario con los valores del resultado del test de las variables contra el target
    '''
    mi = {}
    for col in lista_cat:
        mi_var = mutual_info_score(train[col], train[target_col])
        mi[col] = mi_var
    return mi


def mutual_information_features(df_original, lista_cat):
    '''
    Analiza el test Mutual Information para ver reflejado si existe colinealidad entre las features

    Argumentos:
    df_original(pd.Dataframe): Df original o set de entrenamiento.
    lista_cat(list): Listado de variables que se quiere analizar

    Retorna:
    resultados(dict): Diccionario donde las claves son las relaciones entre las variables y como valor el resultado del test
    '''
    resultados = {}
    for col1 in lista_cat:
        for col2 in lista_cat:
            if col1 != col2:
                mi_var = mutual_info_score(df_original[col1], df_original[col2])
                resultados[f'{col1};{col2}'] = mi_var
    df_colinealidad_mi = pd.DataFrame(list(resultados.items()), columns=['Variables', 'MI'])
    df_colinealidad_mi
        
    return df_colinealidad_mi


def log_transform(X):
    '''
    Esta función realiza una transformación logarítmica manejando valores negativos y 0s

    Argumentos:
    X (pd.Series): variable que se quiere transformar

    Retorna:
    Devuelve la tranformación logarítmica
    '''
    shift = np.abs(X.min()) + 1  # Desplazar para evitar valores <= 0
    return np.log1p( X+ shift)


def columns_transformed(select_feature,df_processed):
    '''
    Genera los nombres de las columnas ya procesadas para poder realizar un entrenamiento correcto y coincidan todos los elementos.

    Argumentos:
    select_feature(list[str]): lista de variables no procesadas
    df_processed(pd.DataFrame): DF de los datos procesados.

    Retorna:
    new_features_lis(list[str]): lista de los nombres de las variables procesadas
    '''
    new_features_list = []
    # Iteramos sobre las columnas originales y reemplazamos con las nuevas
    for feature in select_feature:
        # Buscamos columnas que contengan 'feature' en su nombre dentro de las columnas procesadas
        columns = [col for col in df_processed if feature in col]
        if columns: # Si encontramos columnas que coinciden, las añadimos
            new_features_list.extend(columns)
        else: # Si no hay columnas que coincidan, mantenemos la columna original
            new_features_list.append(feature)
    return(new_features_list)