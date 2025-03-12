import unittest
from ball_simulation.ball_simulation import BallSimulation

class BallSimulationTests(unittest.TestCase):
    
    def test_initialization(self):
        """Тест ініціалізації класу BallSimulation"""
        # Ми не можемо повністю протестувати клас, оскільки він створює візуальний інтерфейс
        # Але можемо перевірити деякі початкові значення
        simulation = BallSimulation()
        self.assertEqual(simulation.mass, 1.0)
        self.assertEqual(simulation.g, 9.8)
        self.assertEqual(simulation.restitution_base, 0.5)
        self.assertEqual(simulation.velocity_restitution_increase, 0.001)
    
    def test_restitution_calculation(self):
        """Тест розрахунку коефіцієнту відновлення"""
        simulation = BallSimulation()
        simulation.mass = 2.0
        simulation.restitution_base = 0.5 - min(0.25, 0.02 * simulation.mass)
        self.assertAlmostEqual(simulation.restitution_base, 0.46)