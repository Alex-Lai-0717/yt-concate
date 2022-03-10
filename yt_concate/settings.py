import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

DOWNLOADS_DIR = 'Download'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'Videos')
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'Captions')
