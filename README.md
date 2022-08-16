
Prediction on streaming medical data

Requirements: 
kafka==1.3.5 
kafka_python==2.0.2 
numpy==1.19.5 
pandas==1.4.3 
pycaret==2.3.10 
pymongo==3.12.0

## This project is about instant analysis of stream data.

The existence of this project is thanks to the pycaret library. I think it is an unusual project.

First, I used a dataset with 70K samples. You can also access this dataset via kaggle.

Kaggle: https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset

An imbalanced data compatible with real life, the performance of many improved models is around 70%.

![](https://github.com/turkalpmd/stream-medical-data/blob/master/Screenshot%20from%202022-08-16%2011-50-09.png)

Using the classifier of the pycaret library, I reached the highest result with the gradientboosting algorithm, and this had an accuracy of around 70% as you can see on kaggle.

After this process, I optimized the model with pycaret and saved it.

I opened a new topic with Kafdrop on Docker.

![](https://github.com/turkalpmd/stream-medical-data/blob/master/Screenshot%20from%202022-08-16%2012-03-59.png)

Then I set up a data_generator that selects random data from the data I reserved for testing. From here, I created a kafka_producer that can send data at random times. I then collected the data I streamed with Kafka_producer with Kafka_consumer. I instantly predicted the data read by Kafka_consumer with the saved model. I was able to collect the last data and transfer it to mongoDB thanks to the pymongo library.
Some tricks about pymongo

    1 - we connect to mongoDB with pymongo via link provided via mongoDB
    2 - In the meantime, it is important to give the ip address of your local computer.
    3 - This video is very helpful to understand the topic: https://youtu.be/GJCKIGeK3qc

![](https://github.com/turkalpmd/stream-medical-data/blob/master/Screenshot%20from%202022-08-16%2012-15-53.png)
![](https://github.com/turkalpmd/stream-medical-data/blob/master/Screenshot%20from%202022-08-16%2012-16-05.png)
![](https://github.com/turkalpmd/stream-medical-data/blob/master/Screenshot%20from%202022-08-16%2013-00-37.png)


Then you can update your model by getting the data collected in mongoDB.

you can review with pymongo_extractor.ipynb

Even for 1354 patients, it has an accuracy of around 70%.
