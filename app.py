import os

from dotenv import load_dotenv
from openai import OpenAI
from PyPDF2 import PdfReader
import gradio as gr

load_dotenv()
# Set up OpenAI with environment variable (Heroku-style)
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

# Build system prompt
system_prompt = f"You are acting as {name}. You are answering questions on {name}'s website, \
particularly questions related to {name}'s career, background, skills and experience. \
Your responsibility is to represent {name} for interactions on the website as faithfully as possible. \
You are given a summary of {name}'s background and LinkedIn profile which you can use to answer questions. \
Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
If you don't know the answer, say so."

system_prompt += f"\n\n## Summary:\n{summary}\n\n## LinkedIn Profile:\n{linkedin}\n\n"
system_prompt += f"With this context, please chat with the user, always staying in character as {name}."

# Chat function
def chat(message, history):
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return response.choices[0].message.content

gr.ChatInterface(chat, type="messages").launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)