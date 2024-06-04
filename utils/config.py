import os

from dotenv import load_dotenv


load_dotenv()

RERANK_API_MODEL = os.getenv("RERANK_API_MODEL")
RERANK_API_BASE = os.getenv("RERANK_API_BASE")
RERANK_API_KEYS = os.getenv("RERANK_API_KEYS").split(",")

RERANK_WINDOW_SIZE = int(os.getenv("RERANK_WINDOW_SIZE"))
RERANK_STEP_SIZE = int(os.getenv("RERANK_STEP_SIZE"))
