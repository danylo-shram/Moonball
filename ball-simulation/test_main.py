import pytest
import sys
import os

# Додаємо шлях до src/main/python у Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../main/python'))

from main import calculate_gravity, calculate_restitution

def test_calculate_gravity():
    """Перевіряємо правильність обчислення гравітації."""
    assert calculate_gravity(5, 9.8) == pytest.approx(9.8 * 1.5)
    assert calculate_gravity(0, 9.8) == pytest.approx(9.8)

def test_calculate_restitution():
    """Перевіряємо правильність обчислення коефіцієнта відновлення."""
    assert calculate_restitution(5) == pytest.approx(0.5 - 0.1)
    assert calculate_restitution(20) == pytest.approx(0.5 - 0.25)
