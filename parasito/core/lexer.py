"""
Módulo Lexer para Parásito Esolang.
Extrae comentarios del código anfitrión mediante tokenize de Python
y los divide según la Regla de la Imparidad (Capa Parásito y Capa Fantasma).
"""

import io
import re
import tokenize
from typing import List, Tuple, Dict, Any


def clean_word(word: str) -> str:
    """Limpia puntuación y espacios de una palabra para normalizar comandos."""
    return word.lower().strip(' ,.!?:;"\'()[]{}')


def sanitize_raw(word: str) -> str:
    """
    Conserva el valor literal exacto. Si el valor venía entrecomillado,
    elimina únicamente las comillas delimitadoras respetando signos de puntuación internos.
    """
    w = word.strip()
    if len(w) >= 2 and ((w.startswith('"') and w.endswith('"')) or (w.startswith("'") and w.endswith("'"))):
        return w[1:-1]
    return w.strip(' ,;()[]{}.!?')


def tokenize_comment_text(text: str) -> List[str]:
    """
    Tokeniza el texto de un comentario respetando cadenas entrecomilladas con espacios
    (ej: '"ACCESO CONCEDIDO"' o '"Bucle Iniciado:"').
    """
    tokens = []
    # Regex para extraer o bien cadenas entrecomilladas ("..." o '...') o palabras individuales
    pattern = r'(?:"[^"]*"|\'[^\']*\'|\S+)'
    matches = re.findall(pattern, text)
    for m in matches:
        tokens.append(m.strip())
    return tokens


def extract_comments_from_source(source_code: str) -> List[str]:
    """
    Extrae todos los comentarios de un script Python usando el módulo estándar tokenize.
    """
    comments = []
    try:
        source_bytes = source_code.encode('utf-8')
        readline = io.BytesIO(source_bytes).readline
        tokens = tokenize.tokenize(readline)
        for tok in tokens:
            if tok.type == tokenize.COMMENT:
                comment_body = tok.string.lstrip('#').strip()
                if comment_body:
                    comments.append(comment_body)
    except Exception as e:
        # Fallback con regex en caso de código sintácticamente incompleto
        for line in source_code.splitlines():
            idx = line.find('#')
            if idx != -1:
                c = line[idx+1:].strip()
                if c:
                    comments.append(c)
    return comments


def extract_layers_from_file(file_path: str) -> Tuple[List[str], List[str], List[str]]:
    """
    Lee un archivo Python y separa sus 3 capas:
    - comments: Lista de comentarios brutos.
    - odd_words: Instrucciones de la VM Parásito (posiciones 1ª, 3ª, 5ª...).
    - even_words: Pegamento gramatical y Capa Fantasma (posiciones 2ª, 4ª, 6ª...).
    """
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    comments = extract_comments_from_source(content)
    full_comment_text = " ".join(comments)
    tokens = tokenize_comment_text(full_comment_text)

    # Regla de la Imparidad:
    # Índice 0 (1ª palabra) -> IMPAR (Capa Parásito)
    # Índice 1 (2ª palabra) -> PAR (Capa Fantasma)
    odd_words = tokens[0::2]
    even_words = tokens[1::2]

    return comments, odd_words, even_words
