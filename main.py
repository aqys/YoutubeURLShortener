import re

def shorten_youtube_url(youtube_url):
    # Match video ID in the YouTube URL
    video_id_regex = re.compile(r'v=([a-zA-Z0-9_-]{11})')
    
    # Search for ID using regex
    match = video_id_regex.search(youtube_url)
    
    if match:
        video_id = match.group(1)
        short_url = f"https://youtu.be/{video_id}"
        return short_url
    else:
        return "Invalid YouTube URL"


youtube_url = input("Enter the YouTube URL: ")
short_url = shorten_youtube_url(youtube_url)
print(f"Shortened URL: {short_url}")
