"""
Núcleo del motor de Parásito Esolang.
"""

from .lexer import (
    extract_comments_from_source,
    extract_layers_from_file,
    tokenize_comment_text,
    clean_word,
    sanitize_raw
)
from .steganography import (
    extract_ghost_acrostic,
    synthesize_steganographic_comment,
    DICCIONARIO_PEGAMENTOS
)
from .vm import ParasitoVM, ExecutionResult, INSTRUCTION_SET
from .infector import infect_target_file, infect_directory

__all__ = [
    "extract_comments_from_source",
    "extract_layers_from_file",
    "tokenize_comment_text",
    "clean_word",
    "sanitize_raw",
    "extract_ghost_acrostic",
    "synthesize_steganographic_comment",
    "DICCIONARIO_PEGAMENTOS",
    "ParasitoVM",
    "ExecutionResult",
    "INSTRUCTION_SET",
    "infect_target_file",
    "infect_directory"
]
