from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

#  to download the video from youtube
#yd = yt.streams.get_highest_resolution()

#yd.download('./yt_downloads')