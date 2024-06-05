import os

from dotenv import load_dotenv


load_dotenv()

LLM_API_MODEL = os.getenv("LLM_API_MODEL")
LLM_API_BASE = os.getenv("LLM_API_BASE")
LLM_API_KEYS = os.getenv("LLM_API_KEYS").split(",")

RERANK_WINDOW_SIZE = int(os.getenv("RERANK_WINDOW_SIZE"))
RERANK_STEP_SIZE = int(os.getenv("RERANK_STEP_SIZE"))
