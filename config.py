import os
from dotenv import load_dotenv

# Load variables from .env file (if it exists)
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

if not GOOGLE_API_KEY:
    print("[WARNING] GOOGLE_API_KEY is not set. "
          "Copy .env.example to .env and add your key.")
