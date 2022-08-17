Requirements: 
* python==3.9.12
* kafka==1.3.5 
* kafka_python==2.0.2 
* numpy==1.19.5 
* pandas==1.4.3 
* pycaret==2.3.10 
* pymongo==3.12.0

## This project is about instant analysis of stream data.


The existence of this project is thanks to the pycaret library. I think it is an unusual project.


![](https://github.com/turkalpmd/stream-medical-data/blob/master/images/unnamed1.png)

## Kafka

Originally developed by LinkedIn, Kafka was opened sourced in 2011 to the Apache Software Foundation where it graduated from the Apache Incubator on October 23rd, 2012. The distributed event store and streams-processing platform was named after the author Franz Kafka by its lead developer, Jay Kreps, because it is a “system optimized for writing.”

## Zookeeper

ZooKeeper, on the other hand, was originally developed by Yahoo in the early 2000s, and started out as a Hadoop sub-project. It was originally developed to manage and streamline big data cluster processes and fix bugs that were occurring during the deployment of distributed clusters. In 2008, it was gifted to the Apache Software Foundation and was promoted soon thereafter to a top-level ASF project.

## MongoDB

MongoDB is an open-source document database and leading NoSQL database. MongoDB is written in C++. This tutorial will give you great understanding on MongoDB concepts needed to create and deploy a highly scalable and performance-oriented database.

Some tutorial links;

[Here is](https://docs.confluent.io/5.1.3/streams/quickstart.html) usefull tutorial for kafka and zookeeper
[Here is](https://www.tutorialspoint.com/mongodb/index.htm) usefull tutorial for mongoDB


## Lets start this project!

#### Firstly install docker on your local
#### Then you must installing docker desktop
#### Then use image for this with docker-compose 

* docker install: https://www.youtube.com/watch?v=aMKUuaga85A

* docker kafka and zookeeper installing: https://youtu.be/WnlX7w4lHvM

* docker desktop installing https://www.youtube.com/watch?v=Vplj9b0L_1Y

## You can find the image file of Kafka, Zookeeper and Kafdrop as [docker-compose.yaml in the code folder](https://github.com/turkalpmd/stream-medical-data/blob/master/code/docker-compose.yaml).

## Now open a MongoDB account if Kafka Zookeeper is running on Docker.

* This video is very helpful to understand the topic: https://youtu.be/GJCKIGeK3qc

### Some tricks about pymongo

* 1 - we connect to mongoDB with pymongo via link provided via mongoDB
* 2 - In the meantime, it is important to give the ip address of your local computer.
    

![](https://github.com/turkalpmd/stream-medical-data/blob/master/images/Screenshot%20from%202022-08-16%2012-15-53.png)
![](https://github.com/turkalpmd/stream-medical-data/blob/master/images/Screenshot%20from%202022-08-16%2012-16-05.png)
![](https://github.com/turkalpmd/stream-medical-data/blob/master/images/Screenshot%20from%202022-08-16%2013-00-37.png)


### Lets creating model!


I used a dataset with 70K samples. You can also access this dataset via kaggle.

[Kaggle](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset)

An imbalanced data compatible with real life, the performance of many improved models is around 70%.

Our results:

![](hhttps://github.com/turkalpmd/stream-medical-data/blob/master/images/Screenshot%20from%202022-08-16%2011-50-09.png)


#### Raw data and preprocessed data in the [data folder](https://github.com/turkalpmd/stream-medical-data/tree/master/data). 




Using the classifier of the pycaret library, I reached the highest result with the gradientboosting algorithm, and this had an accuracy of around 70% as you can see on kaggle. (Model creating notebook in the [code file](https://github.com/turkalpmd/stream-medical-data/blob/master/code/model.ipynb))




After this process, I optimized the model with pycaret and [saved it](https://github.com/turkalpmd/stream-medical-data/blob/master/code/model.pkl).


### Lets create stream data

I opened a new topic with Kafdrop on Docker.






![](https://github.com/turkalpmd/stream-medical-data/blob/master/images/Screenshot%20from%202022-08-16%2012-03-59.png)





* Then I set up a data_generator that selects random data from the data I reserved for testing. From here, I created a kafka_producer that can send data at random times. I then collected the data I streamed with Kafka_producer with Kafka_consumer. I instantly predicted the data read by Kafka_consumer with the saved model. I was able to collect the last data and transfer it to mongoDB thanks to the pymongo library.

## I now accept that; pycaret is installed, kafka, kafdrop and zookeeper are running on docker and you are a member of mongoDB.

* 1- Firstly run [kafka_producer.py](https://github.com/turkalpmd/stream-medical-data/blob/master/code/kafka_producer.py)
*   - This code create data from test data. And push to Kafka topic


* 2- Then run [kafka_mongo_consumer.py](https://github.com/turkalpmd/stream-medical-data/blob/master/code/kafka_mongo_consumer.py)
    * - This code reading to Kafka topic 
    * - Then predicting
    * - Then adding timestamp
    * - Then push to your MongoDB database


* 3- You can collecting data on MongoDB with [pymongo_extraction](https://github.com/turkalpmd/stream-medical-data/blob/master/code/pymongo_extraction.ipynb)
    * - You can use this data for creating new success model for real data
    * - Even for 1354 patients, it has an accuracy of around 70%.