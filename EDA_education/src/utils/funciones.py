import pandas as pd



def limpieza_datos(df, distrito, curso_escolar): # Limpiar datos de primaria y ESO
    df["Distrito"] = distrito
    df["Curso_escolar"] = curso_escolar
    df.rename(columns={"Textbox16": "Total"}, inplace = True)
    df.drop(columns=["CentrosAM2", "CentrosAM3", "TITULARIDAD_CONCIERTO2", "Textbox15"], inplace = True)
    df.drop_duplicates(["Niveles"], keep="first", inplace=True)
    return df


def convertir_valor(df): # Convertir las cifras de primaria y eso
    df["Total"] = df["Total"].astype(str)
    df["Total"] = pd.to_numeric(df["Total"].str.replace(".", ""))
    return df

def limpieza_ti(df): # Limpiar las tablas de la tasa de idoneidad
    df.drop(columns=["SEXO"], inplace=True)
    df.drop([0,1], axis=0, inplace=True)
    df = df.T
    df.reset_index(inplace=True)
    df.rename(columns={"index": "Tasas", 2: "Total"}, inplace=True)
    df["Total"] = df["Total"].str.replace("%","").str.replace(",", ".").astype(float)
    return df

def añadir_tasa(df, df_ti, curso, distrito): # Filtrar para poder añadir la tasa de idoneidad
    global df_filtro # Lo pongo global para que pueda acceder adecuadamente a la función 'obtener_tasa'
    global niveles_indice
    global df_tasa
    df_tasa = df_ti
    df_filtro = df.loc[(df["Curso_escolar"] == curso) & (df["Distrito"] == distrito)]
    niveles = list(df.Niveles.unique())
    niveles_indice = {}
    for i, nivel in enumerate(niveles):
        niveles_indice[nivel] = i
    
    df.loc[df_filtro.index, "Tasa_idoneidad_%"] = df_filtro["Niveles"].apply(obtener_tasa)

def obtener_tasa(nivel): # Añadir las tasas
    indice = niveles_indice.get(nivel)
    if indice is not None:
        return df_tasa["Total"].iloc[indice]
    else:
        return None

def dato_renta_2014(var, distrito): # Obtener renta del 2014 de cada distrito
    df_economia_2014 = pd.read_excel("./data/socio_economico/panel_indicadores_distritos_barrios_2018.xls", sheet_name= distrito)
    var = df_economia_2014.iloc[48,4]
    return var

def dato_renta_2020(var, distrito):
    df_economia_2020 = pd.read_excel("./data/socio_economico/panel_indicadores_distritos_barrios_2023.xlsx", sheet_name= distrito)
    var = df_economia_2020.iloc[53,5]
    return var

def cardinalidad(df_in, umbral_categoria, umbral_continua): # Tipificación de las variables de un DF
    df_tipificacion = pd.DataFrame({
        'Card': df_in.nunique(),  # Cardinalidad
        '%_Card': df_in.nunique() / len(df_in) * 100,  # Porcentaje de cardinalidad
        'Tipo': df_in.dtypes  # Tipo de dato
    })
    
    df_tipificacion["Clasificación_como"] = ""
    
    for col in df_tipificacion.index:
        card = df_tipificacion.loc[col, 'Card']
        porcentaje = df_tipificacion.loc[col, '%_Card']
                
        if card == 2:
            df_tipificacion.at[col, "Clasificación_como"] = "Binaria"
        elif card < umbral_categoria:
            df_tipificacion.at[col, "Clasificación_como"] = "Categórica"
        else:
            if porcentaje >= umbral_continua:
                df_tipificacion.at[col, "Clasificación_como"] = "Numérica Continua"
            else:
                df_tipificacion.at[col, "Clasificación_como"] = "Numérica Discreta"
    
    return df_tipificacion

def categorizar_nivel(nivel): # Categorización de la variable 'Niveles'
    if "Primaria" in nivel:
        return 'Primaria'
    if 'ESO' in nivel:
        return "ESO"
