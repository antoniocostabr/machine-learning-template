import os, random
from pathlib import Path
import numpy as np
import logging

def seed_everything(seed: int = 42) -> None:
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch  # optional
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    except ModuleNotFoundError:
        pass

def ensure_dirs(*paths: str | os.PathLike) -> None:
    for p in paths:
        Path(p).mkdir(parents=True, exist_ok=True)


def configure_logger(
    logger_name: str = __name__,
    log_file_path: str | os.PathLike | None = None,
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO",
) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging._nameToLevel.get(log_level))

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s- %(module)s - %(name)s -  Message: %(message)s"
    )

    if log_file_path is not None:
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger