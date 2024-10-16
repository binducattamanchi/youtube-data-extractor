import os

API_KEY = os.environ.get('YOUTUBE_API_KEY', 'AIzaSyBkHq7Qk0GCe7qR1IJemgW4G3ASFIBCpHw')
KAFKA_BROKER = os.environ.get('KAFKA_BROKER', 'kafka:29092')
KAFKA_TOPIC = 'youtube_data_topic'
S3_BUCKET = 'youtube-data-bucket'
S3_ENDPOINT_URL = os.environ.get('S3_ENDPOINT_URL', 'http://localhost:4566')


#https://github.com/SatadruMukherjee/Data-Preprocessing-Models/blob/main/news_fetcher_etl.py
#https://www.youtube.com/watch?v=oH-O7rrwnOg&t=187s
#https://medium.com/@satadru1998/break-into-data-engineering-100-free-and-100-project-based-ce5d6ee54d03
#https://console.cloud.google.com/apis/api/youtube.googleapis.com/metrics?project=youtube-fetch-438020&supportedpurview=project&pageState=(%22duration%22:(%22groupValue%22:%22PT6H%22,%22customValue%22:null))
#https://developers.google.com/youtube/v3/docs/?apix=true