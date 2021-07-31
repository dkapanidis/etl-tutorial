import logging
import quotes_etl

from setup_logging import setupLogging

setupLogging()

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    quotes_etl.run()
