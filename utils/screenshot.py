from datetime import datetime
from utils.logger import logger


def capture_screenshot(page, test_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = (
        f"screenshots/{test_name}_{timestamp}.png"
    )

    page.screenshot(path=file_path)
    logger.info(
    f"Screenshot captured: {file_path}"
)

    return file_path

