from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = 'web page project'
    videos = 'some videos'
    articles = 'some articles'
    return render_template('project.html', name=name, videos=videos, articles=articles)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
