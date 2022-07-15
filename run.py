"""Run script for app."""
import uvicorn
from dotenv import load_dotenv

from app.main import app

load_dotenv('.env')

PORT = 8000

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=PORT)
