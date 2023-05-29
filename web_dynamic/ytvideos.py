#!/usr/bin/python3

from googleapiclient.discovery import build

# Set up the API client
api_key = 'AIzaSyBNIhR7lu4wVxYmzHJYcruvrfeO6z9k_ME'
youtube = build('youtube', 'v3', developerKey=api_key)

# Define the parameters for the API request
request = youtube.search().list(
    part='snippet',
    maxResults=10,  # Number of videos to retrieve
    q='cooking',  # Keyword for cooking videos
    type='video'
)

# Execute the API request
response = request.execute()

# Extract relevant information from the API response
videos = []
for item in response['items']:
    video = {
        'title': item['snippet']['title'],
        'video_id': item['id']['videoId']
    }
    videos.append(video)

# Process the retrieved videos (e.g., display them on your website)
for video in videos:
    print(video['title'], video['video_id'])
