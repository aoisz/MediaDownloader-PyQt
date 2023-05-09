from pytube import YouTube

link = "https://youtu.be/XgDCYG9su7A"
yt = YouTube(link)
streams = yt.streams.filter(only_video=True)
for stream in streams:
    if stream.mime_type == "video/mp4":
        print(stream.resolution)
print(f'Thumbnail: {yt.thumbnail_url}')