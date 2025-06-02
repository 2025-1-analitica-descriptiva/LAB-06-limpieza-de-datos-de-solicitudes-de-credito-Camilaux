"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

from homework.load_data import load_data
from homework.processing_data import processing_data
from homework.save_data import save_data

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    # Cargar el archivo CSV
    df = load_data()
    
    # Preprocesar los datos
    df = processing_data(df)  

    # Verificar si está la carpeta output si no crearla
    save_data(df)

