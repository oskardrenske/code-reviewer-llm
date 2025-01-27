import time
from loguru import logger
import ollama
import file_handler
import settings


class CodeReviewer:
    def __init__(self):
        self.path_to_check = settings.path_to_check
        self.timestamp = time.strftime("%Y-%m-%d-%H%M%S", time.localtime())
        self.files_to_check = file_handler.get_files_to_check(self.path_to_check)
        self.result_dir = file_handler.create_review_results_dir(
            self.path_to_check, self.timestamp
        )

        file_handler.init_result_file(
            self.result_dir, "review.txt", self.path_to_check, self.timestamp
        )

    def start_review(self):
        for file in self.files_to_check:
            logger.warning(file)
            review = self.llm(file_handler.read_file(file))

            file_handler.write_rewiev_result(
                self.result_dir, settings.review_file_name, review, file
            )

    def llm(self, file_content):
        ollama_response = ollama.chat(
            model=settings.llm_model,
            messages=[
                {
                    "role": "system",
                    "content": settings.system_prompt,
                },
                {"role": "user", "content": f"{settings.user_prompt} {file_content}"},
            ],
            options={"temperature": settings.temperature},
        )
        return ollama_response["message"]["content"]
