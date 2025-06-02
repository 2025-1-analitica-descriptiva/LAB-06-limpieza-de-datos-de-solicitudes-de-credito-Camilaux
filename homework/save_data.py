import os


def save_data(df):
    output_dir = "files/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Guardar el DataFrame limpio en un nuevo archivo CSV
    df.to_csv("files/output/solicitudes_de_credito.csv", sep=";")