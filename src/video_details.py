

def get_video_details(youtube, video_id):
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    )
    response = request.execute()

    if 'items' in response:
        video = response['items'][0]
        details = {
            'title': video['snippet']['title'],
            'publishedAt': video['snippet']['publishedAt'],
            'views': video['statistics']['viewCount'],
            'likes': video['statistics'].get('likeCount', 0),
            'comments': video['statistics'].get('commentCount', 0)
        }
        return details
    else:
        return None
