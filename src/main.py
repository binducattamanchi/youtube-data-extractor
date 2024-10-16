import logging
from config.config import API_KEY, KAFKA_BROKER, KAFKA_TOPIC, S3_BUCKET, S3_ENDPOINT_URL
from src import get_video_comments,get_video_details,create_youtube_client, get_channel_stats,create_kafka_producer, send_to_kafka,create_s3_client, ensure_bucket_exists, upload_to_s3


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    youtube = create_youtube_client(API_KEY)
    kafka_producer = create_kafka_producer(KAFKA_BROKER)
    s3_client = create_s3_client(S3_ENDPOINT_URL)

    ensure_bucket_exists(s3_client, S3_BUCKET)

    channel_username = "sumitmittal07"
    video_id = "Q4nbwea22jo"

    # Get channel stats
    channel_stats = get_channel_stats(youtube, channel_username)
    if channel_stats:
        send_to_kafka(kafka_producer, channel_stats, f"{KAFKA_TOPIC}_channel_stats")
        upload_to_s3(s3_client, channel_stats, S3_BUCKET, f"channel_stats/{channel_username}.json")

    # Get video details
    video_details = get_video_details(youtube, video_id)
    if video_details:
        send_to_kafka(kafka_producer, video_details, f"{KAFKA_TOPIC}_video_details")
        upload_to_s3(s3_client, video_details, S3_BUCKET, f"video_details/{video_id}.json")

    # Get video comments
    comments = get_video_comments(youtube, video_id, max_results=10)
    if comments:
        send_to_kafka(kafka_producer, comments, f"{KAFKA_TOPIC}_video_comments")
        upload_to_s3(s3_client, comments, S3_BUCKET, f"video_comments/{video_id}.json")

if __name__ == "__main__":
    main()