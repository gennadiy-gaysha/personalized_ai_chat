import os

from dotenv import load_dotenv
from openai import OpenAI
from PyPDF2 import PdfReader
import gradio as gr
from datetime import datetime

load_dotenv()
# Connect to Gemini via OpenAI-compatible endpoint
google_api_key = os.getenv("GEMINI_API_KEY")
gemini = OpenAI(
    api_key=google_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
model_name = "gemini-2.0-flash"

# Read LinkedIn PDF
reader = PdfReader("me/linkedin.pdf")
linkedin = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        linkedin += text

# Read summary text
with open("me/summary.txt", encoding="utf-8") as f:
    summary = f.read()

name = "Gennadiy Gaysha"

# Chat function
def chat(message, history):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    dynamic_prompt = f"""You are acting as {name}. You are answering questions on {name}'s website, \
    particularly questions related to {name}'s career, background, skills and experience. \
    Your responsibility is to represent {name} for interactions on the website as faithfully as possible. \
    You are given a summary of {name}'s background and LinkedIn profile which you can use to answer questions. \
    Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
    If you don't know the answer, say so. Always answer in a language the same to the language that you was asked in!

    The current date and time is: {now}

    ## Summary:
    {summary}

    ## LinkedIn Profile:
    {linkedin}

    With this context, please chat with the user, always staying in character as {name}.
    """

    messages = [{"role": "system", "content": dynamic_prompt}] + history + [{"role": "user", "content": message}]
    response = gemini.chat.completions.create(model=model_name, messages=messages)
    return response.choices[0].message.content

gr.ChatInterface(chat, type="messages").launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)