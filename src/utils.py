import os, random
from pathlib import Path
import numpy as np

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