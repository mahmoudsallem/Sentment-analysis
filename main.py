## Import Librarise
from fastapi import FastAPI
# from utils import response
from transformers import pipeline
from googletrans import Translator

from transformers import logging
logging.set_verbosity_error()


# ## Initialize an app
app = FastAPI(debug=True)

pipe = pipeline("sentiment-analysis")
# pipe = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")


# Create a translator object
translator = Translator()


# Function to translate text to English
def translate_to_english(text):
    translation = translator.translate(text, dest='en')
    return translation.text


def analysis(text: str):
    resp = pipe(text)
    return resp


# ## The Function
@app.post('/SentementAnalysis')
async def chatbot(prompt: str):

    prompt = translate_to_english(prompt)
    ## Call the function from utils.py file
    response = analysis(prompt)

    return response