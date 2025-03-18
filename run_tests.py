import unittest

# Виконуємо пошук тестів у всьому проєкті
loader = unittest.TestLoader()
suite = loader.discover(start_dir="src/unittest/python", pattern="*.py")  # Шукає всі тестові файли

runner = unittest.TextTestRunner()
runner.run(suite)

