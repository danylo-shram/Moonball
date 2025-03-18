import unittest
from src.main.python.main import calculate_gravity, calculate_restitution

class TestBallSimulation(unittest.TestCase):
    def test_calculate_gravity(self):
        """Перевіряємо правильність обчислення гравітації."""
        self.assertAlmostEqual(calculate_gravity(5, 9.8), 9.8 * 1.5)
        self.assertAlmostEqual(calculate_gravity(0, 9.8), 9.8)

    def test_calculate_restitution(self):
        """Перевіряємо правильність обчислення коефіцієнта відновлення."""
        self.assertAlmostEqual(calculate_restitution(5), 0.5 - 0.1)
        self.assertAlmostEqual(calculate_restitution(20), 0.5 - 0.25)

if __name__ == "__main__":
    unittest.main()
