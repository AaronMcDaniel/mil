import os

from mil.data.datasets.loader import load_data

current_file = os.path.abspath(os.path.dirname(__file__))
def load():
    return load_data(os.path.join(current_file, './csv/musk1.csv'))
    