from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is a web page project. It works!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
