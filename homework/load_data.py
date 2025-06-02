import pandas as pd


def load_data():
    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";")
    return df