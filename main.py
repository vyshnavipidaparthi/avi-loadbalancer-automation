import yaml
import logging
import os
from framework.test_runner import run_test, parallel_run

# === Setup Logging ===
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "output.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file, mode="w"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# === Load Config ===
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

if __name__ == "__main__":
    logger.info("=== Avi Load Balancer Test Framework Started ===")

    try:
        if config["tests"]["parallel"]:
            logger.info("Running tests in parallel mode...")
            parallel_run(config["tests"]["num_threads"])
        else:
            logger.info("Running single test execution...")
            run_test(1)

        logger.info("=== Test Execution Completed Successfully ===")

    except Exception as e:
        logger.error(f" Framework encountered an error: {e}")
