from loguru import logger
from code_reviewer import CodeReviewer


def main():
    logger.info("start")
    reviewer = CodeReviewer()
    reviewer.start_review()
    logger.info(f"Finished, read report file: {reviewer.result_file}")


if __name__ == "__main__":
    main()
