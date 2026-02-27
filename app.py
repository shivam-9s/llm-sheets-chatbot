import gradio as gr
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# ============================
# Load DialoGPT Locally
# ============================
print("Loading DialoGPT model locally...")

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

print("DialoGPT Loaded Successfully")

# ============================
# Google Sheets Setup
# ============================
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json", scope
)

client_sheet = gspread.authorize(creds)
sheet = client_sheet.open("ChatbotLogs").sheet1

print("Google Sheet Connected Successfully")

# ============================
# Chat Function
# ============================
def chatbot(user_input):

    # Save user input
    sheet.append_row(["User", user_input])

    # Encode input
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

    # Generate response
    output_ids = model.generate(
        input_ids,
        max_length=200,
        pad_token_id=tokenizer.eos_token_id
    )

    reply = tokenizer.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

    # Save AI reply
    sheet.append_row(["AI", reply])

    return reply

# ============================
# Gradio UI
# ============================
ui = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(placeholder="Type your message..."),
    outputs="text",
    title="Chatbot",
    description="Runs locally without Hugging Face API limits"
)

ui.launch()
