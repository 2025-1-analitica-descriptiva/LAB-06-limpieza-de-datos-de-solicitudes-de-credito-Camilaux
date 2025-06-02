import pandas as pd


def processing_data(df):
    df = df.drop(columns=['Unnamed: 0'])

    # Verificar valores de la columna 'sexo'
    # print("Valores únicos en la columna 'sexo':", df['sexo'].unique())
    df['sexo'] = df['sexo'].str.lower()  # Convertir a minúsculas

    #Verificar valores de la columna 'tipo_de_emprendimiento'
    #print("Valores únicos en la columna 'tipo_de_emprendimiento':", df['tipo_de_emprendimiento'].unique())
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower() # Convertir a minúsculas

    # Verificar valores de la columna 'idea_negocio'
    # print("Valores únicos en la columna 'idea_negocio':", df['idea_negocio'].unique())
    df['idea_negocio'] = df['idea_negocio'].str.lower()  # Convertir a minúsculas
    # eliminar espacios en blanco al inicio y al final de las cadenas y caracteres especiales "_" y "-"
    df['idea_negocio'] = df['idea_negocio'].str.replace('_', ' ').str.replace('-', ' ').str.strip()

    # Verificar valores de la columna 'barrio'
    # print("Valores únicos en la columna 'barrio':", df['barrio'].unique())
    df['barrio'] = df['barrio'].str.lower()  # Convertir a minúsculas
    # Eliminar espacios en blanco al inicio y al final de las cadenas
    df['barrio'] = df['barrio'].str.replace('_', ' ').str.replace('-', ' ')

    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)  # Convertir a cadena

    # Convertir a datetime la columna 'fecha_de_beneficio'
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True, errors='coerce', format='mixed')

    # Eliminar "$" de la columna 'monto_del_credito' y convertir a entero
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('$','')
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',','')
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('.00','')
    df['monto_del_credito'] = df['monto_del_credito'].str.strip()

    # Verificar valores de la columna 'línea_credito'
    # print("Valores únicos en la columna 'línea_credito':", df['línea_credito'].unique())
    df['línea_credito'] = df['línea_credito'].str.lower()  # Convertir a minúsculas
    # Eliminar espacios en blanco al inicio y al final de las cadenas
    df['línea_credito'] = df['línea_credito'].str.strip().str.replace('_', ' ').str.replace('-', ' ').str.strip()

    # Eliminar registros duplicados
    df.drop_duplicates(inplace=True)

    df.dropna(inplace=True)
    return df