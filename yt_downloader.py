from pytubefix import YouTube

url = input("Enter video URL: ")
path = ""

yt = YouTube(url)

stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

stream.download(path)


# ! Wherever you save this project, it will store the videos you download in that folder.!
