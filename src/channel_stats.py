from googleapiclient.discovery import build

def create_youtube_client(api_key):
    return build('youtube', 'v3', developerKey=api_key)

def get_channel_stats(youtube, channel_id):
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=channel_id
    )
    response = request.execute()

    if 'items' in response:
        channel = response['items'][0]
        stats = {
            'title': channel['snippet']['title'],
            'subscribers': channel['statistics']['subscriberCount'],
            'views': channel['statistics']['viewCount'],
            'totalVideos': channel['statistics']['videoCount']
        }
        return stats
    else:
        return None


