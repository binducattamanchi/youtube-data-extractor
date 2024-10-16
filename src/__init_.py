# __init__.py

# Import key functions or classes from your modules
from .video_comments import create_youtube_client, get_video_comments
from .video_details import create_youtube_client, get_video_details
from .channel_stats import create_youtube_client, get_channel_stats
from .kafka_producer import create_kafka_producer, send_to_kafka
from .s3_uploader import create_s3_client, upload_to_s3

# You can define __all__ to control what's imported with "from package import *"
__all__ = [
    'create_youtube_client',
    'get_video_details',
    'get_video_comments',
    'create_kafka_producer',
    'send_to_kafka',
    'create_s3_client',
    'upload_to_s3'
]

# Package-level configurations or initializations
YOUTUBE_API_VERSION = 'v3'
KAFKA_TOPIC_PREFIX = 'youtube_data_'

# You can also include any package-level initialization code
print(f"Initializing YouTube Data Extraction package")
