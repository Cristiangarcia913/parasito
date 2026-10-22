import unittest
from parasito.core.steganography import (
    extract_ghost_acrostic,
    synthesize_steganographic_comment
)


class TestSteganography(unittest.TestCase):
    def test_extract_acrostic(self):
        even_words = ["Servidor", "Enlace", "Conexion", "Registro", "Entrada", "Transmision"]
        ghost = extract_ghost_acrostic(even_words)
        self.assertEqual(ghost, "SECRET")

    def test_synthesize_comment(self):
        instructions = ["limpiar", "guardar", "10", "mostrar"]
        secret_ghost = "HACK"
        comment = synthesize_steganographic_comment(instructions, secret_ghost)
        words = comment.split()
        self.assertEqual(len(words), 8)
        # Palabras pares deben formar HACK
        even_words = words[1::2]
        ghost = extract_ghost_acrostic(even_words)
        self.assertEqual(ghost, "HACK")


if __name__ == "__main__":
    unittest.main()
