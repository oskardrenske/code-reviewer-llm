import os
from pathlib import Path
from loguru import logger
import settings


def read_file(file_path):
    with open(file_path, mode="r", encoding="utf-8") as f:
        return f.read()


def init_result_file(output_dir, output_file_name, path_to_check, timestamp):
    with open(output_dir / output_file_name, "w") as f:
        f.write(f"Review of {path_to_check}\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"System prompt {settings.system_prompt}\n")
        f.write("------------------------------------\n")
        logger.info(f"Initialized {output_dir / output_file_name}")


def write_rewiev_result(output_dir, output_file_name, result, file_path):
    with open(output_dir / output_file_name, "a", encoding="utf-8") as f:
        f.write(f"{file_path}\n")
        f.write(result)
        f.write("\n---------------------------\n\n")


def get_files_to_check(directory_path):
    file_paths = []
    current_dir = os.path.join(os.getcwd(), directory_path)
    """Walk through all directories recursively and find files matching the desired suffix"""
    for root, dirs, files in os.walk(current_dir):
        if "venv" in root:
            continue
        for file in files:
            if file.endswith(settings.file_suffix) and not file.startswith("_"):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
    logger.info(f"Found {len(file_paths)} matching files")
    return file_paths


def create_review_results_dir(path_to_check, date_str):
    product = convert_path_to_dash(path_to_check)

    product_dir = Path(f"reviews/{product}")
    product_dir.mkdir(parents=True, exist_ok=True)

    date_dir = Path(f"{product_dir}/{date_str}")
    date_dir.mkdir(parents=True, exist_ok=True)
    return date_dir


def convert_path_to_dash(path_string: str) -> str:
    """
    convert forward slash and backslash to dash
    """
    new_char = "-"
    converted = path_string.replace("\\", new_char).replace("/", new_char)
    if converted.startswith(new_char):
        converted = converted[1:]
    if converted.endswith(new_char):
        converted = converted[:-1]
    return converted
