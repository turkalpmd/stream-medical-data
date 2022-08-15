import pandas as pd
import numpy as np

df = pd.read_csv("/home/izzet/Desktop/stream-medical-data/all_preprocessed_data.csv")
demographic_info = pd.read_csv("/home/izzet/Desktop/stream-medical-data/MOCK_DATA.csv")

def data_creator():
    main = df.iloc[np.random.randint(0,df.shape[0])]
    demographic = demographic_info.iloc[np.random.randint(demographic_info.shape[0])]
    return pd.concat([demographic,main],axis=0).to_json()

# for i in range(10):
#     if __name__ == '__main__':
#          print(data_creator())