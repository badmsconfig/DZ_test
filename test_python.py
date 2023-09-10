import math
import pytest

# Тесты для функции filter
def test_filter_even_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = list(filter(lambda x: x % 2 == 0, numbers))
    assert result == [2, 4, 6, 8, 10]

def test_filter_positive_numbers():
    numbers = [-2, -1, 0, 1, 2]
    result = list(filter(lambda x: x > 0, numbers))
    assert result == [1, 2]

def test_filter_empty_list():
    numbers = []
    result = list(filter(lambda x: x > 0, numbers))
    assert result == []

def test_filter_all_true():
    numbers = [1, 2, 3]
    result = list(filter(lambda x: x > 0, numbers))
    assert result == [1, 2, 3]

# Тесты для функции map
def test_map_square():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x**2, numbers))
    assert result == [1, 4, 9, 16, 25]

def test_map_double():
    numbers = [2, 4, 6, 8, 10]
    result = list(map(lambda x: x * 2, numbers))
    assert result == [4, 8, 12, 16, 20]

def test_map_empty_list():
    numbers = []
    result = list(map(lambda x: x * 2, numbers))
    assert result == []

# Тесты для функции sorted
def test_sorted_ascending():
    numbers = [5, 2, 9, 1, 5]
    result = sorted(numbers)
    assert result == [1, 2, 5, 5, 9]

def test_sorted_descending():
    numbers = [5, 2, 9, 1, 5]
    result = sorted(numbers, reverse=True)
    assert result == [9, 5, 5, 2, 1]

def test_sorted_empty_list():
    numbers = []
    result = sorted(numbers)
    assert result == []

# Тесты для функций из библиотеки math
def test_math_pi():
    assert math.isclose(math.pi, 3.141592653589793, rel_tol=1e-9)

def test_math_sqrt():
    result = math.sqrt(16)
    assert result == 4.0

def test_math_pow():
    result = math.pow(2, 3)
    assert result == 8.0

def test_math_hypot():
    result = math.hypot(3, 4)
    assert result == 5.0

def test_math_sqrt_negative_input():
    with pytest.raises(ValueError):
        math.sqrt(-1)
