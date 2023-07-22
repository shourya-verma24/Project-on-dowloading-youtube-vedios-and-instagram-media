#import pytube
from pytube import YouTube
URL = input("Paste your VIDEO LINK Here:", )   # TAKING INPUT FROM USER
yt = YouTube(URL)
print(yt.title)
print(yt.thumbnail_url)
streamsAll = yt.streams.all()
mp4 = yt.streams.filter(file_extension="mp4").all()
print("mp4 vedios are",mp4)
is_hd = input("do you want to download hd, Yes/No", )
if is_hd == "Yes":
    hd = yt.streams.get_by_itag(("22"))
    hd.download()
    print("Downloaded IN HD")
else:
    datasaver = yt.streams.get_by_itag(("18"))
    datasaver.download()
    print("Downloaded IN datasaver mode")