from pathlib import Path
RANDOM_SEED = 42
N_FOLDS = 5
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_ROOT / "data" / "corpus_features.csv"
RESULTS_DIR = PROJECT_ROOT / "results"
