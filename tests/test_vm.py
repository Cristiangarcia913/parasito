import unittest
from parasito.core.vm import ParasitoVM


class TestVM(unittest.TestCase):
    def setUp(self):
        self.vm = ParasitoVM(sandbox_mode=True)

    def test_arithmetic(self):
        # guardar 10 sumar 5 multiplicar 2 mostrar
        instructions = ["guardar", "10", "sumar", "5", "multiplicar", "2", "mostrar"]
        res = self.vm.execute_tokens(instructions)
        self.assertEqual(res.output, "30")

    def test_strings(self):
        # guardar "HOLA_" unir "MUNDO" mostrar
        instructions = ["guardar", "HOLA_", "unir", "MUNDO", "mostrar"]
        res = self.vm.execute_tokens(instructions)
        self.assertEqual(res.output, "HOLA_MUNDO")

    def test_variables(self):
        # guardar 42 archivar x guardar 0 recordar x mostrar
        instructions = ["guardar", "42", "archivar", "x", "guardar", "0", "recordar", "x", "mostrar"]
        res = self.vm.execute_tokens(instructions)
        self.assertEqual(res.output, "42")

    def test_loop(self):
        # guardar 3 archivar c destino loop recordar c mostrar restar 1 archivar c revisar loop
        instructions = [
            "guardar", "3", "archivar", "c",
            "destino", "loop",
            "recordar", "c", "mostrar",
            "restar", "1", "archivar", "c",
            "revisar", "loop"
        ]
        res = self.vm.execute_tokens(instructions)
        self.assertEqual(res.output, "321")


if __name__ == "__main__":
    unittest.main()
