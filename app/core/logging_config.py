
import logging.config

from app.core.config import get_settings


def configure_logging() -> None:
    settings = get_settings()

    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": (
                        "%(asctime)s | %(levelname)-8s | "
                        "%(name)s | %(message)s"
                    ),
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "standard",
                    "level": "DEBUG",
                }
            },
            "root": {
                "level": settings.log_level.upper(),
                "handlers": ["console"],
            },
        }
    )
