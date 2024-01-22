from flask import Flask, request, render_template, Response , send_file ,url_for
from utils.gpt import gpt
from utils.prompt import generatePrompt
from utils.dalle import dallE
from utils.t2s import textSpeech
from dotenv import load_dotenv
import os
import base64
import io
import base64
from flask import send_from_directory


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


# @app.route('/static/<filename>')
# def serve_image(filename):
#     return send_from_directory('static', filename)

 # make function to extract prompt from text [slice??]
    # img = dallE(dalle_prompt,PAT)
     # aud= textSpeech(text,PAT)
     
# @app.route('/image/<filename>')
# def serve_image(filename):
#     return send_file(filename, mimetype='image/jpg')
# with open("output_image.png", "wb") as f:
    #  f.write(img)
    # return "hello"



if __name__ == '__main__':
    app.run(debug=True)





