## LLM Sheets Chatbot

**LLM Sheets Chatbot** is a lightweight AI chatbot application that runs locally using a Large Language Model and stores all conversations automatically in **Google Sheets**. The project demonstrates how to integrate **LLMs, a web interface, and cloud-based data storage** to build a simple conversational AI system with persistent logging.

The chatbot is built with **Python and Gradio** to provide an interactive web interface where users can ask questions and receive AI-generated responses. Each interaction between the user and the AI is captured and stored in a connected **Google Sheet**, enabling easy tracking, analysis, or monitoring of conversations.

This project highlights practical integration between **Natural Language Processing (NLP), APIs, and cloud services**, making it a useful example of how conversational AI systems can be combined with external data storage for real-world applications.

---

## Key Features

* **Local AI Chatbot** powered by a Large Language Model
* **Interactive UI** built using Gradio
* **Automatic conversation logging** to Google Sheets
* **Secure API integration** using Google Service Account credentials
* **Simple and lightweight architecture** suitable for learning and experimentation

---

## Technologies Used

* **Python**
* **Gradio** – for building the chatbot interface
* **Hugging Face Transformers / LLM** – for generating responses
* **Google Sheets API (gspread)** – for storing conversation logs
* **dotenv** – for managing environment variables

---

## How It Works

1. The user enters a message in the chatbot interface.
2. The input is sent to a **local Large Language Model** for processing.
3. The model generates a response.
4. The conversation (user query + AI response) is appended to a **Google Sheet**.
5. The response is displayed in the chatbot interface.

---

## Project Structure

```
LLM_Sheets_Chatbot
│
├── app.py              # Main chatbot application
├── test_sheet.py       # Script to test Google Sheets connection
├── requirements.txt    # Project dependencies
├── credentials.json    # Google Sheets API credentials (not included in repo)
├── .env                # Environment variables
└── venv/               # Virtual environment
```

---

## Setup Instructions

1. Clone the repository

```
git clone https://github.com/your-username/llm-sheets-chatbot.git
```

2. Navigate to the project directory

```
cd llm-sheets-chatbot
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Add your **Google Sheets API credentials** file (`credentials.json`).

5. Run the chatbot

```
python app.py
```

6. Open the interface in your browser

```
http://127.0.0.1:7860
```

---

## Future Improvements

* Add conversation history memory
* Deploy the chatbot online
* Add a database for long-term storage
* Improve UI with a chat-style interface
* Integrate RAG (Retrieval Augmented Generation)

---

