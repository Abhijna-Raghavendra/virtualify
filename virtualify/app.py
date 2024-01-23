from flask import Flask, request, render_template, Response , send_file ,url_for
from utils.gpt import gpt
from utils.prompt import generatePrompt
from utils.dalle import dallE
from utils.t2s import textSpeech
from dotenv import load_dotenv
import os

load_dotenv()

PAT = os.getenv("PAT")

app = Flask(__name__,
            static_url_path='/static', 
            static_folder='static',
            template_folder='templates',
            )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/story/<genre>')
def story(genre):
    name = request.args.get("name")
    description = request.args.get("description")
    gpt_prompt = generatePrompt(name,description,genre)
    
    text= gpt(gpt_prompt,PAT)
    img = dallE(text+"in 1280X960", PAT)
    img = dallE(text, PAT)
    img_path = os.path.join(os.getcwd(), "virtualify/static", "img.png")
    os.makedirs(os.path.dirname(img_path), exist_ok=True)
    with open(img_path, "wb") as f:
        f.write(img)
    
    aud= textSpeech(text,PAT)
    aud_path = os.path.join(os.getcwd(), "virtualify/static", "aud.wav")
    os.makedirs(os.path.dirname(aud_path), exist_ok=True)
    with open(aud_path , 'wb') as f:
         f.write( aud)
        
    return render_template('story.html',text=text)

@app.route('/process_text', methods=['POST'])
def process_text():
    # Retrieve user input from the form
    user_text = request.form.get('user_text')
    
    # Process the user_text using your GPT model
    # genre = "your_genre"  # Replace with the actual genre you want to use
    # gpt_prompt = generatePrompt("name", "description", genre, user_text)
    text = gpt(user_text, PAT)

    # Update the image and audio files based on the generated text
    img = dallE(text + "in 1280X960", PAT)
    img_path = os.path.join(os.getcwd(), "virtualify/static", "img.png")
    with open(img_path, "wb") as f:
        f.write(img)

    aud = textSpeech(text, PAT)
    aud_path = os.path.join(os.getcwd(), "virtualify/static", "aud.wav")
    with open(aud_path, 'wb') as f:
        f.write(aud)
    # return "hello"
    return render_template('story.html',text=text)

if __name__ == '__main__':
    app.run(debug=True)





