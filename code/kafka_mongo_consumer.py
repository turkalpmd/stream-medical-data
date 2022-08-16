import json 
import pandas as pd
from time import sleep
from datetime import date, datetime
from kafka import KafkaConsumer
from pycaret.classification import load_model
from pycaret.classification import*
import pymongo


conn_str = "mongodb+srv://<username>:<password>@medical.5ml64kh.mongodb.net/?retryWrites=true&w=majority"


try:
     client = pymongo.MongoClient(conn_str)
except Exception:
     print("Error: " + str(Exception))

# # Create DataBase Section

myDb = client["stream_medical_data"]

# # Create DataBase Collection

myCollection =myDb["cardiac_failure"]

# path name must be same with producer.
model = load_model("code/model.pkl")

if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        'Heart_Failure_Project', # topic name !!!!
        bootstrap_servers='localhost:9092',
        group_id = None,
        auto_offset_reset='earliest')

    for message in consumer:
        # firstly load to consumer data then transfer to pandas dataframe
        stream_data = pd.DataFrame(pd.read_json(json.loads(message.value),typ="dict")).T
        #print(prediction_data)
        target = stream_data["target"]
        stream_data.drop(columns="target",inplace=True)
        prediction = predict_model(model,stream_data)
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        prediction["target"] = target
        prediction["time"] = dt_string
        values = []
        for i in prediction.values:
            for j in i:
                values.append(j)
        keys = list(prediction.keys())
        msg = dict(zip(keys, values))
        json_msg = json.dumps(msg, indent = len(keys))
        print(msg)
        if target.values == prediction.Label.values:
            print("Prediction is True!")
        else:
            print("Prediction is False")
        res = myCollection.insert_one(json.loads(json_msg))
        print(res.inserted_id)