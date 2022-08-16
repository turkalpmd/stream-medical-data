import pandas as pd
import numpy as np

df = pd.read_csv("data/cardio_train.csv")


def data_creator():
    new_df = df.iloc[np.random.randint(0,df.shape[0])]
    return new_df.to_json()
    

# for i in range(1):
#     if __name__ == '__main__':
#          print(data_creator())