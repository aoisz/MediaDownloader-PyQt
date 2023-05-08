from pytube import YouTube

link = "https://www.youtube.com/watch?v=bAbOVCiAOEU"
yt = YouTube(link)
streams = yt.streams.filter(only_video=True)
for stream in streams:
    print(stream.resolution)