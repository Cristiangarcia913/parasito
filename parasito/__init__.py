"""
Parásito: Lenguaje de Programación Esteganográfico & Motor de Infección
=====================================================================

Autor: Cristian García (@Cristiangarcia913)
Versión: 2.0.0
Licencia: MIT

Tres realidades superpuestas en un único archivo:
- Capa 1: Código Anfitrión (ejecución estándar de Python)
- Capa 2: Código Parásito (instrucciones esolang en posiciones impares de los comentarios)
- Capa 3: Capa Fantasma (acróstico esteganográfico en iniciales de palabras pares)
"""

from typing import Dict, Any, Optional
from .core.lexer import extract_layers_from_file
from .core.steganography import extract_ghost_acrostic, synthesize_steganographic_comment
from .core.vm import ParasitoVM, ExecutionResult
from .core.infector import infect_target_file, infect_directory

__version__ = "2.0.0"
__author__ = "Cristian García"


def run_file(file_path: str, sandbox_mode: bool = False) -> ExecutionResult:
    """
    Ejecuta el código Parásito contenido en los comentarios del archivo objetivo.
    """
    comments, odd_words, even_words = extract_layers_from_file(file_path)
    vm = ParasitoVM(sandbox_mode=sandbox_mode)
    return vm.execute_tokens(odd_words, even_words)


def inspect_file(file_path: str) -> Dict[str, Any]:
    """
    Inspecciona y descompone las 3 capas de un archivo Python anfitrión.
    """
    comments, odd_words, even_words = extract_layers_from_file(file_path)
    ghost = extract_ghost_acrostic(even_words)
    return {
        "file": file_path,
        "total_comments": len(comments),
        "raw_comments": comments,
        "parasite_instructions": odd_words,
        "ghost_words": even_words,
        "ghost_acrostic": ghost
    }


def despertar(file_path: str):
    """
    Punto de entrada compatible con las demos originales:
    Despierta al Parásito, ejecuta su VM e imprime la salida y el acróstico.
    """
    res = run_file(file_path, sandbox_mode=False)

    print("\n========================================")
    print("  🦠 [PARÁSITO] EJECUCIÓN DEL ESOLANG")
    print("========================================")
    print(res.output if res.output else "(El parásito guardó silencio)")
    print("----------------------------------------")

    if res.ghost_message:
        print("\n👻 [FANTASMA] ESCÁNER DE ACRÓSTICOS (Capa Par)")
        print(f"Mensaje acróstico oculto: {res.ghost_message}")
        print("========================================\n")


__all__ = [
    "ParasitoVM",
    "ExecutionResult",
    "run_file",
    "inspect_file",
    "despertar",
    "infect_target_file",
    "infect_directory",
    "synthesize_steganographic_comment",
    "__version__",
    "__author__"
]
