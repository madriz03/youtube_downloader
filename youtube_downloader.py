import yt_dlp

def download(link):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s'  # Nombre del archivo igual al título del video
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

video = input('Enter the YouTube link here URL:  ')
download(video)
