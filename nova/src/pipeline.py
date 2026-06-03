import json
from pathlib import Path

from nova.src.ingestion import fetch_data
from nova.src.validation import validate_records
from nova.src.logger import get_logger

logger = get_logger(__name__)

URL = "https://dummyjson.com/carts"


def save_json(data: list, file_path: Path) -> None:

    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def run_pipeline() -> None:

    logger.info("Pipeline started")

    logger.info("Fetching data...")

    records = fetch_data(URL)

    logger.info(f"Fetched {len(records)} records")

    valid_records, invalid_records = validate_records(records)

    logger.info(f"Valid Records: {len(valid_records)}")
    logger.info(f"Invalid Records: {len(invalid_records)}")

    save_json(
        valid_records,
        Path("nova/data/validated/records.json")
    )

    save_json(
        invalid_records,
        Path("nova/data/rejected/rejected_records.json")
    )

    logger.info("Saved validated records")
    logger.info("Saved rejected records")

    logger.info("pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()