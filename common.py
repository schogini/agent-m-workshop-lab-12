import os
from pathlib import Path
from dotenv import load_dotenv
from agno.models.openrouter import OpenRouter

load_dotenv(Path(__file__).parent / ".env")

MODEL_ID = os.getenv("MODEL_ID", "openrouter/free")
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "BAAI/bge-small-en-v1.5",
)

def make_model():
    """Create the workshop's OpenRouter model.

    OPENROUTER_API_KEY is read automatically by Agno.
    The default model id `openrouter/free` dynamically selects a free model.
    """
    return OpenRouter(id=MODEL_ID)
