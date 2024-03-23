from pytube import YouTube

def download_video_from_youtube(link, path):
    yt = YouTube(link)
    video = yt.streams.get_by_resolution_var()

    # download the video
    video.download(path)

# example usage:
download_video_from_youtube('https://www.youtube.com/watch?v=111GAE55swI', 'Downloads')