import os
import random

from pytube import YouTube
from youtube_search import YoutubeSearch


def download_audio(link):
    print(f"Downloading video... {link}")
    out_file = f"{random.randint(0, 100000)}.mp3"
    yt = YouTube(link)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path="temp", filename=out_file)
    data = {'file': os.path.join("temp", out_file),
            'title': yt.title,
            'channel': yt.author,
            'duration': yt.length,
            'thumbnail': yt.thumbnail_url,
            'link': link}
    return data


def get_music(search):
    if "youtube.com" in search:
        return download_audio(search)
    else:
        results = YoutubeSearch(search, max_results=10).to_dict()
        if len(results) > 0:
            result = results[0]
            data = download_audio("https://www.youtube.com/" + result['url_suffix'])
            return data
