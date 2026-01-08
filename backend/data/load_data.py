import pandas as pd
from pathlib import Path

def load_data():
    data_path = Path(__file__).resolve().parents[2] / "dataset" / "student_performance.csv"
    df = pd.read_csv(data_path)
    return df
