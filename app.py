from flask import Flask , render_template , request ,redirect
from mp3_baixar import baixando_mp3_app
app = Flask(__name__)

#primeira página
@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/mp3')
def download_mp3():
    return render_template("mp3.html")

@app.route('/mp3/baixando' , methods=['POST'])
def baixando_mp3():
    link = request.form.get('input')
    baixando_mp3_app(link)
    return redirect('/mp3')

@app.route('/mp4')
def download_mp4():
    return render_template("mp4.html")

@app.route('/mp4/baixando' , methods=['POST'])
def baixando_mp4():
    link = request.form.get('input')
    print(link)
    return redirect('/mp4')

#rodar site
if __name__ == '__main__':

    app.run(debug=True)
