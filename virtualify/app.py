from flask import Flask, request, render_template
from utils.gpt import gpt
from utils.prompt import generatePrompt
from utils.dalle import dallE
from utils.t2s import textSpeech
from dotenv import load_dotenv
import os

load_dotenv()

PAT = os.getenv("PAT")

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/story/<genre>')
def story(genre):
    name = request.args.get("name")
    description = request.args.get("description")

    gpt_prompt = generatePrompt(name,description,genre)
    text = gpt('two liner description of '+genre,PAT)
    # make function to extract prompt from text [slice??]
    dalle_prompt = ''
    img = dallE(dalle_prompt)
    aud = textSpeech(text)
    return text

if __name__ == '__main__':
    app.run(debug=True)
