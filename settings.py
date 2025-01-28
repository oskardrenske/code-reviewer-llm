import os
from loguru import logger

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

llm_model = os.getenv("LLM_MODEL", None)
file_suffix_env_var = os.getenv("FILE_SUFFIX", ".py, .md")
file_suffixes = [ft.strip() for ft in file_suffix_env_var.split(",")]
programming_language = os.getenv("PROG_LANG", "python")
path_to_check = os.getenv("PATH_TO_CHECK", None)
tone = os.getenv("TONE", "neutral")


system_prompt = f"You are a {programming_language} expert specialized in code reviews."
user_prompt = f"Review the following {programming_language} code and markdown content in a {tone} tone and give helpful advice on how to improve it: "


output_dir = "reviews"
review_file_name = "review.txt"

PRINT = os.getenv("PRINT", "True").lower() == "true"

temperature = 0


if llm_model is None:
    raise ValueError("no LLM model specified as environment variable")
if path_to_check is None:
    raise ValueError("no path to code specified as environment variable")

logger.info(f"System prompt: {system_prompt}")
logger.info(f"User prompt: {user_prompt} + file content")
logger.info("Loaded settings and environment variables")
