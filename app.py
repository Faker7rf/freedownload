from flask import Flask , render_template , request ,redirect, send_file
from pytube import YouTube
import os
import time
app = Flask(__name__)

#primeira página
@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/mp3')
def download_mp3():
    
    return render_template("mp3.html")


@app.route('/mp3/baixando' , methods=['POST'])
def baixando_mp3_app():
    try:
        link = request.form.get('input')
        print(link)
        url_audio = YouTube(link)
        # print("\nBaixando....")
        video = url_audio.streams.filter(only_audio=True).first()
        name = video.title + ".mp3"
        
        out_file = video.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        print("\nDownload completo...\n")
        name_config = name.replace('/' , '')
        print(name_config)
        return redirect(f'/arquivo/{name_config}')
    except:
        return 'Insira um link!!'
    
@app.route('/arquivo/<filename>' , methods=['GET'])
def arquivo_mp3(filename):
    file = os.path.join(filename)
    return send_file(file, as_attachment=True)

@app.route('/mp4')
def download_mp4():
    return render_template("mp4.html")

@app.route('/mp4/baixando' , methods=['POST'])
def baixando_mp4():
    try:
        link = request.form.get('input')
        print(link)
        url_video = YouTube(link)
        video = url_video.streams.get_highest_resolution()
        video.download()
        name = video.title
        name_config = name.replace('/' , '')
        return redirect(f'/arquivo/{name_config}.mp4')
    except:
        return 'Insira um link!!'

#rodar site
if __name__ == '__main__':

    app.run(debug=True)

