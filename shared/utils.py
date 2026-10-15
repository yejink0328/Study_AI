"""여러 주제에서 재사용하는 유틸 함수 모음.

노트북에서 사용:
    import sys; sys.path.append("../../..")   # 저장소 루트까지의 상대경로는 위치에 맞게 조정
    from shared.utils import DATA_DIR, set_seed
"""
import os
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"


def set_seed(seed: int = 42) -> None:
    """재현성을 위한 시드 고정."""
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    try:
        import numpy as np
        np.random.seed(seed)
    except ImportError:
        pass
    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass
