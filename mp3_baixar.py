from pytube import YouTube
import os

def baixando_mp3_app(link):
 
    url_audio = YouTube(link)

    try:
        print("\nBaixando....")
        video = url_audio.streams.filter(only_audio=True).first()
        out_file = video.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        print("\nDownload completo...\n")

    except:
        print("\nOcorreu um erro, verifique se o link está correto e tente novamente....\n")