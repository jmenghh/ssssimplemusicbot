import youtube_dl
import os  # os모듈
from youtubesearchpython import VideosSearch

file = './song.mp3'  # 파일 경로 설정


def ydl(name):

    url = VideosSearch(str(name), limit=1)
    link = url.resultComponents
    result = link[0]['link']
    if os.path.isfile(file):  # song.mp3파일이 존재하면
        os.remove(file)  # 파일 삭제


    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': 'song.mp3',
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([result])