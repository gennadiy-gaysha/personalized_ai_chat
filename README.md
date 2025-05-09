# **My Personalized AI Chatbot**
(You can view the live site here - [My Personalized AI Chatbot](https://personalized-ai-chat-ef6db309de9d.herokuapp.com/))

## Overview

This project creates a personalized AI-powered chatbot representing **Gennadiy Gaysha** as Junior Full Stack Java Developer. The chatbot answers questions related to Gennadiy’s career, skills, background, and experience, using the context from his **LinkedIn profile** and a **summary**. The app is built using **Gradio** for the frontend interface, with **Gemini AI** (Google's advanced AI model) integrated via the OpenAI API.

The chatbot uses **dynamic time and date** to ensure responses are time-sensitive and reflects real-time interaction.

---

## Features

* **Personalized Chatbot**: The AI represents **my person** in conversation, based on my professional background, skills, and LinkedIn profile.
* **Time-Sensitive Responses**: The current time and date are dynamically integrated into the chat responses.
* **Gradio Interface**: The chatbot is powered through an easy-to-use Gradio interface for simple interaction.
* **Gemini API**: The backend uses Google’s Gemini model `gemini-2.0-flash`, accessed via OpenAI-compatible endpoints, to generate responses.

---

## Installation

### Prerequisites

1. **Python 3.8+**
2. **API Key**: You’ll need to sign up for the **Google Gemini API** and get your API key. You can obtain it [here](https://developers.google.com/generative-language).
3. **Gradio**: For the interactive chat interface.
4. **PyPDF2**: To extract data from the LinkedIn PDF.

### Steps

1. **Clone the Repository**:

   ```bash
   git clone <repo-url>
   cd <repo-directory>
   ```

2. **Install Dependencies**:
   Create a virtual environment and install the required Python packages:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For MacOS/Linux
   venv\Scripts\activate     # For Windows
   pip install -r requirements.txt
   ```

   Make sure to install these libraries if you don’t have them in your `requirements.txt`:

   ```bash
   pip install openai gradio python-dotenv PyPDF2
   ```

3. **Set Up Environment Variables**:

   * Create a `.env` file in the root directory and add the following:

     ```
     GEMINI_API_KEY=your-google-api-key
     PORT=7860
     ```
   * Replace `your-google-api-key` with your actual **Google Gemini API Key**.

4. **Prepare LinkedIn Profile and Summary**:

   * Place your **LinkedIn PDF** in the `me/` directory as `linkedin.pdf`.
   * Place a **summary text file** in the `me/` directory as `summary.txt`. This file should contain a brief summary of Gennadiy Gaysha’s professional background.

---

## Usage

After setting up the project, run the following command to start the app:

```bash
python app.py
```

This will launch the Gradio interface on `http://localhost:7860` (or the Heroku-provided URL if deployed).

### How It Works:

1. The AI chatbot uses the **LinkedIn PDF** and **summary.txt** as sources of information about Gennadiy Gaysha.
2. The current date and time are dynamically injected into the conversation prompt, ensuring that the AI remains time-sensitive.
3. The chatbot is integrated with the **Gemini AI** model via OpenAI-compatible endpoints to process and generate responses based on the context provided.

---

## Deployment on Heroku

### Steps to Deploy:

1. **Push to Heroku**:

   ```bash
   git remote add heroku https://git.heroku.com/<your-heroku-app-name>.git
   git push heroku main
   ```

2. **Set Environment Variables on Heroku**:
   Add the necessary environment variables on Heroku using the following commands:

   ```bash
   heroku config:set GEMINI_API_KEY=your-google-api-key
   heroku config:set PORT=7860
   ```

3. **Access the App**:
   Once deployed, you can access the app via the Heroku-provided URL.

---

## Acknowledgments

* **Gradio**: For creating an easy-to-use interface for AI models.
* **Google Gemini API**: For providing powerful generative language models.
* **PyPDF2**: For parsing and extracting data from PDF files.

---
