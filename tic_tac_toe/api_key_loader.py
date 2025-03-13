import os
import requests
from dotenv import load_dotenv

GITHUB_RAW_URL = "https://raw.githubusercontent.com/yourusername/your-private-repo/main/.env"

def fetch_api_key():
    """Fetches .env file containing API key from a private GitHub repo"""
    response = requests.get(GITHUB_RAW_URL)
    
    if response.status_code == 200:
        with open(".env", "w") as f:
            f.write(response.text)
        print("[INFO] .env file downloaded successfully.")
    else:
        print("[ERROR] Failed to fetch API key from GitHub.")

# Fetch .env if it doesn’t exist
if not os.path.exists(".env"):
    fetch_api_key()

# Load environment variables
load_dotenv()
