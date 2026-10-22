import unittest
from parasito.core.lexer import (
    clean_word,
    sanitize_raw,
    tokenize_comment_text,
    extract_comments_from_source
)


class TestLexer(unittest.TestCase):
    def test_clean_word(self):
        self.assertEqual(clean_word("Limpiar,"), "limpiar")
        self.assertEqual(clean_word('"ACCESO"'), "acceso")
        self.assertEqual(clean_word("[DESTINO]"), "destino")

    def test_sanitize_raw(self):
        self.assertEqual(sanitize_raw('"ACCESO_ALPHA"'), "ACCESO_ALPHA")
        self.assertEqual(sanitize_raw("Hola!"), "Hola")

    def test_tokenize_quotes(self):
        tokens = tokenize_comment_text('Limpiar Nodo "TEXTO CON ESPACIOS" Modulo')
        self.assertEqual(len(tokens), 4)
        self.assertEqual(tokens[0], "Limpiar")
        self.assertEqual(tokens[1], "Nodo")
        self.assertEqual(tokens[2], '"TEXTO CON ESPACIOS"')
        self.assertEqual(tokens[3], "Modulo")

    def test_extract_comments(self):
        source = """
# Primer comentario
x = 10  # Comentario en línea
'''Docstring ignorado'''
# Tercer comentario
"""
        comments = extract_comments_from_source(source)
        self.assertIn("Primer comentario", comments)
        self.assertIn("Comentario en línea", comments)
        self.assertIn("Tercer comentario", comments)


if __name__ == "__main__":
    unittest.main()
