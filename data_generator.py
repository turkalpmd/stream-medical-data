import pandas as pd
import numpy as np

df = pd.read_csv("/home/izzet/Desktop/stream-medical-data/all_preprocessed_data.csv")
np.random.seed(100)
def data_creator():
    return df.iloc[np.random.randint(0,df.shape[0])].to_json()

# for i in range(10):
#     if __name__ == '__main__':
#          print(data_creator())