# config.py
import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables
load_dotenv()


class Settings(BaseSettings):
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "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")
    MODEL_NAME: str = "llama-3.3-70b-versatile"
    MAX_TOKENS: int = 1000
    TEMPERATURE: float = 0.7


settings = Settings()