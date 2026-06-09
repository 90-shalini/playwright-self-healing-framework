import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    filename="logs/framework.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    force = True
    # handlers=[
    #     logging.FileHandler("logs/framework.log"),
    #     logging.StreamHandler()
    # ]
)

logger = logging.getLogger()