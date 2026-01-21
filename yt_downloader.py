from pytubefix import YouTube

url = input("Enter video URL: ")

path = ""

YouTube(url).streams.get_highest_resolution().download(path)

##Wherever you save this project, it will store the videos you download in that folder.
