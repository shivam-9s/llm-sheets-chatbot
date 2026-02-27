# 🤖 LLM Sheets Chatbot

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Gradio](https://img.shields.io/badge/Gradio-UI-orange)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
![Google Sheets](https://img.shields.io/badge/Google-Sheets-green)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

An AI-powered chatbot that runs locally using a **Large Language Model (LLM)** and automatically logs conversations into **Google Sheets**.

This project demonstrates how to integrate **LLMs, APIs, and cloud services** to build a conversational AI system with persistent logging and monitoring.

---

# 📌 Project Overview

The **LLM Sheets Chatbot** allows users to interact with an AI chatbot through a **Gradio-based web interface**.

Each interaction between the user and the AI is automatically recorded and stored in **Google Sheets**, allowing easy monitoring, analytics, and tracking of chatbot conversations.

This project demonstrates the practical integration of:

* Large Language Models (LLMs)
* Natural Language Processing
* Web-based Chatbot Interfaces
* Google Cloud APIs
* Cloud-based Data Logging

---

# 🚀 Features

* AI chatbot powered by a **Large Language Model**
* **Interactive UI** built using Gradio
* **Automatic conversation logging** into Google Sheets
* **Local execution** without API rate limits
* **Secure API integration** using Google Service Account credentials
* Lightweight and easy-to-understand architecture

---

# 🧠 Tech Stack

| Technology                | Purpose                                       |
| ------------------------- | --------------------------------------------- |
| Python                    | Core programming language                     |
| Gradio                    | Web interface for chatbot                     |
| Hugging Face Transformers | LLM-based response generation                 |
| Google Sheets API         | Cloud storage for chat logs                   |
| gspread                   | Python library to interact with Google Sheets |
| python-dotenv             | Managing environment variables                |

---

# 🏗 System Architecture

```
User Input
   │
   ▼
Gradio Web Interface
   │
   ▼
LLM Model (Transformers)
   │
   ▼
Generated Response
   │
   ▼
Google Sheets API
   │
   ▼
Conversation Logs Stored
```

---

# 📂 Project Structure

```
LLM_Sheets_Chatbot
│
├── app.py
├── test_sheet.py
├── requirements.txt
├── credentials.json
├── .env
├── .gitignore
└── venv
```

### File Explanation

| File             | Description                             |
| ---------------- | --------------------------------------- |
| app.py           | Main chatbot application                |
| test_sheet.py    | Script to test Google Sheets connection |
| requirements.txt | Python dependencies                     |
| credentials.json | Google Sheets API credentials           |
| .env             | Environment variables                   |
| .gitignore       | Files ignored during Git uploads        |

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/llm-sheets-chatbot.git
```

---

## 2️⃣ Navigate to the Project Directory

```
cd llm-sheets-chatbot
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

# 🔑 Setup Google Sheets API

1. Go to **Google Cloud Console**
2. Enable **Google Sheets API**
3. Create a **Service Account**
4. Download the **credentials.json** file
5. Place it inside the project folder
6. Create a **Google Sheet**
7. Share the sheet with the **service account email**

---

# ▶️ Running the Application

Activate the virtual environment

```
venv\Scripts\activate
```

Run the chatbot

```
python app.py
```

Open the chatbot in your browser

```
http://127.0.0.1:7860
```

---

# 📊 Example Output in Google Sheets

| Role | Message                                                                      |
| ---- | ---------------------------------------------------------------------------- |
| User | Hello                                                                        |
| AI   | Hi! How can I help you today?                                                |
| User | What is Artificial Intelligence?                                             |
| AI   | Artificial Intelligence refers to machines that simulate human intelligence. |

---

# 💡 Use Cases

* AI chatbot experimentation
* Conversation logging and analytics
* Learning LLM integrations
* Customer interaction tracking
* Educational NLP projects

---

# 🔮 Future Improvements

* Add chatbot memory
* Deploy chatbot online
* Implement Retrieval-Augmented Generation (RAG)
* Improve UI design
* Store conversations in a database
* Add user authentication

---

# 🧑‍💻 Skills Demonstrated

* Large Language Model Integration
* API Integration
* Google Cloud Services
* Python Backend Development
* NLP Application Development
* Web Interface Development

---

# 👨‍💻 Author

**Shivam**

Aspiring **Data Scientist / AI Engineer** passionate about building practical AI applications and exploring real-world machine learning systems.

---

# 📜 License

This project is licensed under the **MIT License**.

---

⭐ If you find this project useful, consider **starring the repository**.
