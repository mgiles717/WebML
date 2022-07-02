import os
import pandas as pd

PATH = os.path.dirname(__file__)

def load_migraine():
    return pd.read_csv(f"{PATH}/data/migraine_data.csv")

if __name__ == '__main__':
    print(load_migraine())