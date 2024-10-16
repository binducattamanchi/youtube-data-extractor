import json
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import time
import logging

logger = logging.getLogger(__name__)

def create_kafka_producer(kafka_broker, max_retries=5, retry_delay=5):
    for attempt in range(max_retries):
        try:
            producer = KafkaProducer(
                bootstrap_servers=[kafka_broker],
                api_version=(0, 10, 1),
                request_timeout_ms=5000,
                max_block_ms=5000,
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            return producer
        except NoBrokersAvailable:
            if attempt < max_retries - 1:
                logger.warning(f"No brokers available. Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                logger.error("Failed to connect to Kafka after multiple attempts.")
                raise

def send_to_kafka(producer, data, topic):
    try:
        future = producer.send(topic, data)
        future.get(timeout=10)
        logger.info(f"Sent data to Kafka topic {topic}")
    except Exception as e:
        logger.error(f"Error sending data to Kafka: {e}")