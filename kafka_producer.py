import time 
import json 
import random 
from datetime import datetime
from  data_generator  import data_creator
from kafka import KafkaProducer

def serializer(message):
    return json.dumps(message).encode('utf-8')

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer,
    acks = "all")

if __name__ == '__main__':
    # Infinite loop - runs until you kill the program
    while True:
        # Generate a message
        dummy_message = data_creator()
        
        # Send it to our 'messages' topic
        print(f'Producing message @ {datetime.now()} | Message = {str(dummy_message)}')
        producer.send('Heart_Failure_Project', dummy_message)
        
        # Sleep for a random number of seconds
        time_to_sleep = random.randint(1, 100)
        time.sleep(time_to_sleep)
