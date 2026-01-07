"""Basic test examples for the Python AI Template."""

import numpy as np
import pandas as pd


def test_basic_arithmetic():
    """Test basic arithmetic operations."""
    assert 1 + 2 == 3
    assert 5 - 3 == 2
    assert 4 * 3 == 12
    assert 10 / 2 == 5


def test_numpy_operations():
    """Test basic numpy operations."""
    arr = np.array([1, 2, 3, 4, 5])

    assert arr.sum() == 15
    assert arr.mean() == 3.0
    assert arr.max() == 5
    assert arr.min() == 1


def test_pandas_operations():
    """Test basic pandas operations."""
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

    assert df.shape == (3, 2)
    assert df["A"].sum() == 6
    assert df["B"].mean() == 5.0


class TestClassExample:
    """Example test class to demonstrate class-based testing."""

    def setup_method(self):
        """Setup method called before each test method."""
        self.test_data = [1, 2, 3, 4, 5]

    def test_sum(self):
        """Test sum calculation."""
        assert sum(self.test_data) == 15

    def test_length(self):
        """Test length calculation."""
        assert len(self.test_data) == 5

    def test_max_value(self):
        """Test maximum value."""
        assert max(self.test_data) == 5

    def test_min_value(self):
        """Test minimum value."""
        assert min(self.test_data) == 1
