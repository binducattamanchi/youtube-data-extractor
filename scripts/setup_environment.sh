#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Set up Kafka
docker-compose up -d kafka

# Set up LocalStack (for S3)
docker-compose up -d localstack

echo "Environment setup complete!"