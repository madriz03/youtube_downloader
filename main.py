from pytube import YouTube 

def download(link): 
    videoObject = YouTube(link) 
    videoObject = videoObject.streams.get_highest_resolution() 
    videoObject.download() 

video = input('Enter the youtube link here URL:  ') 
download(video)