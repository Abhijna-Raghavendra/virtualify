from flask import Flask
from utils import prompt, t2s, gpt, dalle

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Vitualify</h1>An AI-driven storytelling platform that generates personalized and engaging narratives across diverse genres.'

@app.route('/story')
def index():
    return '<h1>Storey page</h1>'

if __name__ == '__main__':
    app.run(debug=True)
