import os
import unittest
from parasito import run_file, inspect_file


class TestDemos(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.examples_dir = os.path.join(self.base_dir, "examples")

    def test_demo_auth_ghost(self):
        file_path = os.path.join(self.examples_dir, "01_auth_backdoor.py")
        data = inspect_file(file_path)
        self.assertTrue(data["ghost_acrostic"].startswith("SECRET"))

    def test_demo_turing_loop(self):
        file_path = os.path.join(self.examples_dir, "03_turing_loop.py")
        res = run_file(file_path, sandbox_mode=True)
        self.assertIn("Bucle_Iniciado: 3", res.output)
        self.assertIn("¡Bucle_Completado!", res.output)
        self.assertEqual(res.ghost_message[:5], "CICLO")

    def test_demo_calculator_ghost(self):
        file_path = os.path.join(self.examples_dir, "04_calculator.py")
        data = inspect_file(file_path)
        self.assertTrue("NUMBERS" in data["ghost_acrostic"])


if __name__ == "__main__":
    unittest.main()
