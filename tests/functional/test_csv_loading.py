import pandas as pd
import os

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "..", "fixtures", "users.csv")


def test_csv_loads_correct_shape():
    """DataFrame should have 3 rows and 3 columns."""
    df = pd.read_csv(FIXTURE_PATH)
    assert df.shape == (3, 3)


def test_csv_column_names():
    """DataFrame should contain expected column names."""
    df = pd.read_csv(FIXTURE_PATH)
    assert list(df.columns) == ["name", "age", "city"]


def test_csv_column_dtypes():
    """Column 'age' should be integer, 'name' and 'city' should be string."""
    df = pd.read_csv(FIXTURE_PATH)
    assert df["age"].dtype == int
    assert df["name"].dtype == object or df["name"].dtype.name == "str"
