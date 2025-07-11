import gspread
from google.oauth2.service_account import Credentials

# Define the scopes needed
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 
          'https://www.googleapis.com/auth/drive']

# Load credentials
creds = Credentials.from_service_account_file('credentials.json', scopes=SCOPES)

# Authenticate
client = gspread.authorize(creds)

# Create a new spreadsheet
spreadsheet = client.create('July Reports')

# Share with your Gmail (optional)
spreadsheet.share('your-email@gmail.com', perm_type='user', role='writer')

# Open and write to the first sheet
sheet = spreadsheet.sheet1
sheet.update('A1', 'Date')
sheet.update('B1', 'Revenue')
sheet.update('A2', '2025-07-11')
sheet.update('B2', '₹25,000')

print(f"✅ Sheet Created: {spreadsheet.url}")
