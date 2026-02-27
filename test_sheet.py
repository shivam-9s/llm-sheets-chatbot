import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json", scope)

client = gspread.authorize(creds)

# Open your sheet
sheet = client.open("ChatbotLogs").sheet1

# Add a test row
sheet.append_row(["Test", "Sheet Connected Successfully"])

print("✅ Google Sheet Connected and Row Added!")
