import logging 
from pathlib import Path

def get_logger(name: str) -> logging.Logger:

    log_dir = Path("nova/logs")
    log_dir.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(
                log_dir / "nova.log",
                encoding="utf-8"
            ),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger(name)