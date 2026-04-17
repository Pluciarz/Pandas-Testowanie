import pandas as pd
import os

EMPLOYEES_PATH = os.path.join(os.path.dirname(__file__), "..", "fixtures", "employees.csv")
DEPARTMENTS_PATH = os.path.join(os.path.dirname(__file__), "..", "fixtures", "departments.csv")


def test_merge_contains_all_columns():
    """Merged DataFrame should contain columns from both input DataFrames."""
    employees = pd.read_csv(EMPLOYEES_PATH)
    departments = pd.read_csv(DEPARTMENTS_PATH)
    merged = pd.merge(employees, departments, on="id")
    assert "name" in merged.columns
    assert "department" in merged.columns


def test_inner_merge_row_count():
    """Inner merge should return only rows with matching IDs in both DataFrames."""
    employees = pd.read_csv(EMPLOYEES_PATH)
    departments = pd.read_csv(DEPARTMENTS_PATH)
    merged = pd.merge(employees, departments, on="id", how="inner")
    assert len(merged) == 3


def test_merge_excludes_unmatched_ids():
    """ID present only in one DataFrame should not appear in inner merge result."""
    employees = pd.read_csv(EMPLOYEES_PATH)
    departments = pd.read_csv(DEPARTMENTS_PATH)
    merged = pd.merge(employees, departments, on="id", how="inner")
    assert 4 not in merged["id"].values
    assert 5 not in merged["id"].values