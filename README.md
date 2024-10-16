# YouTube Data Extraction and Analysis Project

## Overview

This project focuses on extracting and analyzing data from YouTube videos using the YouTube Data API. It provides insights into video performance metrics such as comments, subscriber count, likes, comment count, and more. The project utilizes a modern tech stack including Apache Kafka for real-time data streaming, Docker for containerization, AWS S3 for data storage, and PySpark for large-scale data processing.

## Features

- Extract detailed video data including:
  - Comments
  - Subscriber count
  - Like count
  - Comment count
  - Video title and description
  - Channel information
- Real-time data streaming with Apache Kafka
- Scalable data processing with PySpark
- Cloud storage integration with AWS S3
- Containerized environment using Docker

## Tech Stack

- **YouTube Data API**: For extracting video and channel data
- **Apache Kafka**: For real-time data streaming
- **Docker**: For containerization of Kafka and AWS S3 components
- **AWS S3**: For cloud storage of extracted data
- **PySpark**: For large-scale data processing and analysis
- **Python**: Primary programming language

## Prerequisites

- Python 3.7+
- Docker and Docker Compose
- AWS account with S3 access
- YouTube Data API key

## Setup

1. Clone the repository:

`git clone https://github.com/your-username/youtube-data-project.git`
`cd youtube-data-project`

2. Set up YouTube API key:
- Visit Google Developers Console
- Create a new project or select an existing one
- Enable the YouTube Data API v3
- Create credentials (API key)
- Store the API key securely
- Configure environment variables:
- Create a .env file in the project root:

`YOUTUBE_API_KEY=your_api_key_here`
`AWS_ACCESS_KEY_ID=your_aws_access_key`
`AWS_SECRET_ACCESS_KEY=your_aws_secret_key`

3. Start Docker containers:
`docker-compose up -d`

4. Install Python dependencies:
`pip install -r requirements.txt`

5. Usage
