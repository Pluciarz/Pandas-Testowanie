import pandas as pd


def test_dropna_removes_rows_with_nan():
    """Rows containing NaN should be removed by dropna()."""
    df = pd.DataFrame({
        "name": ["Alice", "Bob", None, "Diana"],
        "age": [30, None, 25, 28],
        "city": ["Warsaw", "Krakow", "Gdansk", None]
    })
    cleaned = df.dropna()
    assert len(cleaned) == 1


def test_dropna_result_has_no_nan():
    """Resulting DataFrame should contain no NaN values."""
    df = pd.DataFrame({
        "name": ["Alice", None, "Charlie"],
        "age": [30, 25, None]
    })
    cleaned = df.dropna()
    assert cleaned.isnull().sum().sum() == 0


def test_dropna_row_count_less_than_original():
    """Cleaned DataFrame should have fewer rows than original."""
    df = pd.DataFrame({
        "name": ["Alice", None, "Charlie"],
        "age": [30, 25, None]
    })
    cleaned = df.dropna()
    assert len(cleaned) < len(df)