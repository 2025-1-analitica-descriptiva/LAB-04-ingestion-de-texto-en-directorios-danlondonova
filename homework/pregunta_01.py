
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


import zipfile
import pandas as pd
import os

def pregunta_01():
    # Descomprimir ZIP solo si no existe ya la carpeta
    if not os.path.exists("files/input/train"):
        with zipfile.ZipFile("files/input.zip", "r") as zip_ref:
            zip_ref.extractall("files")

    test = {"phrase": [], "target": []}
    train = {"phrase": [], "target": []}

    # Recorremos todos los archivos .txt
    for root, _, filenames in os.walk("files/input"):
        for file_name in filenames:
            if file_name.endswith(".txt"):
                full_path = os.path.join(root, file_name)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        phrase = f.read().strip()
                except:
                    # En caso de fallo, omitir archivo
                    continue

                target = os.path.basename(os.path.dirname(full_path))  # carpeta: positive/negative/neutral

                if "test" in full_path:
                    test["phrase"].append(phrase)
                    test["target"].append(target)
                elif "train" in full_path:
                    train["phrase"].append(phrase)
                    train["target"].append(target)

    # Convertir a DataFrame
    test_df = pd.DataFrame(test)
    train_df = pd.DataFrame(train)

    # Crear carpeta de salida
    output_dir = "files/output"
    os.makedirs(output_dir, exist_ok=True)

    # Guardar CSVs
    test_df.to_csv(os.path.join(output_dir, "test_dataset.csv"), index=False)
    train_df.to_csv(os.path.join(output_dir, "train_dataset.csv"), index=False)

# Permitir ejecución directa
if __name__ == "__main__":
    pregunta_01()


    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """