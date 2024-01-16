from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Vitualify</h1>An AI-driven storytelling platform that generates personalized and engaging narratives across diverse genres.'

if __name__ == '__main__':
    app.run(debug=True)
