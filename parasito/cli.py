"""
Interfaz de Línea de Comandos (CLI) de Parásito Esolang.
Permite ejecutar, inspeccionar capas, extraer acrósticos y sintetizar código esteganográfico.
"""

import argparse
import os
import sys

# Asegurar codificación UTF-8 en terminales Windows
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from .core.lexer import extract_layers_from_file
from .core.steganography import extract_ghost_acrostic, synthesize_steganographic_comment
from .core.vm import ParasitoVM
from .core.infector import infect_target_file
from . import run_file, inspect_file, __version__


def cmd_run(args):
    """Ejecuta el programa Parásito dentro del archivo indicado."""
    if not os.path.exists(args.file):
        print(f"❌ Error: Archivo '{args.file}' no encontrado.", file=sys.stderr)
        sys.exit(1)

    res = run_file(args.file, sandbox_mode=args.sandbox)

    print("\n" + "=" * 50)
    print("  🦠 [PARÁSITO] EJECUCIÓN DE LA VM")
    print("=" * 50)
    print(res.output if res.output else "(El parásito guardó silencio)")
    print("-" * 50)
    if res.ghost_message:
        print(f"👻 Acróstico Fantasma : {res.ghost_message}")
    print(f"📊 Ciclos ejecutados  : {res.cycles_executed}")
    if res.secret_payload:
        print(f"💉 Payload generado   : {res.secret_payload}")
    if res.error:
        print(f"⚠️ Alerta/Error       : {res.error}")
    print("=" * 50 + "\n")


def cmd_inspect(args):
    """Inspecciona y descompone las 3 capas superpuestas del archivo."""
    if not os.path.exists(args.file):
        print(f"❌ Error: Archivo '{args.file}' no encontrado.", file=sys.stderr)
        sys.exit(1)

    data = inspect_file(args.file)

    print("\n" + "=" * 65)
    print(f"  🔬 DISECCIÓN DE CAPAS ESTEGANOGRÁFICAS: {os.path.basename(args.file)}")
    print("=" * 65)
    print(f"• Total comentarios brutos : {data['total_comments']}")
    print(f"• Tokens Capa Parásito     : {len(data['parasite_instructions'])} (Palabras Impares)")
    print(f"• Tokens Capa Fantasma     : {len(data['ghost_words'])} (Palabras Pares)")
    print(f"• Mensaje Acróstico Oculto : '{data['ghost_acrostic']}'")
    print("-" * 65)

    print("\n[CAPA 2: INSTRUCCIONES EJECUTABLES VM (IMPARES)]")
    ins_preview = " ".join(data['parasite_instructions'][:20])
    if len(data['parasite_instructions']) > 20:
        ins_preview += " ..."
    print(f"  {ins_preview}")

    print("\n[CAPA 3: PEGAMENTO GRAMATICAL Y ACRÓSTICO (PARES)]")
    glue_preview = " ".join(data['ghost_words'][:20])
    if len(data['ghost_words']) > 20:
        glue_preview += " ..."
    print(f"  {glue_preview}")

    print("\n" + "=" * 65 + "\n")


def cmd_ghost(args):
    """Extrae exclusivamente el mensaje de la Capa Fantasma."""
    if not os.path.exists(args.file):
        print(f"❌ Error: Archivo '{args.file}' no encontrado.", file=sys.stderr)
        sys.exit(1)

    _, _, even_words = extract_layers_from_file(args.file)
    ghost = extract_ghost_acrostic(even_words)
    print(ghost)


def cmd_compile(args):
    """Sintetiza un comentario esteganográfico válido."""
    instructions = args.instructions.split()
    ghost_msg = args.ghost

    comment = synthesize_steganographic_comment(instructions, ghost_msg)
    print("\n# " + comment + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Parásito Esolang - Intérprete y Motor de Esteganografía en Código Fuente",
        epilog="Desarrollado por Cristian García (@Cristiangarcia913)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"Parásito {__version__}")
    subparsers = parser.add_subparsers(dest="subcommand", help="Comandos disponibles")

    # Comando run
    p_run = subparsers.add_parser("run", help="Ejecuta el código Parásito dentro de un archivo Python")
    p_run.add_argument("file", help="Ruta al archivo Python anfitrión")
    p_run.add_argument("--sandbox", action="store_true", help="Modo sandbox (no escribe en disco)")

    # Comando inspect
    p_inspect = subparsers.add_parser("inspect", help="Disecciona y visualiza las 3 capas del archivo")
    p_inspect.add_argument("file", help="Ruta al archivo Python anfitrión")

    # Comando ghost
    p_ghost = subparsers.add_parser("ghost", help="Extrae el mensaje acróstico de la Capa Fantasma")
    p_ghost.add_argument("file", help="Ruta al archivo Python anfitrión")

    # Comando compile
    p_compile = subparsers.add_parser("compile", help="Genera un comentario esteganográfico técnico")
    p_compile.add_argument("-i", "--instructions", required=True, help="Lista de instrucciones separadas por espacio")
    p_compile.add_argument("-g", "--ghost", required=True, help="Mensaje secreto para el acróstico par")

    # Comando infect
    p_infect = subparsers.add_parser("infect", help="Inyecta el payload Parásito en un script")
    p_infect.add_argument("target", help="Archivo .py víctima")
    p_infect.add_argument("-g", "--ghost", default="INFILTRADO", help="Mensaje secreto para el acróstico")

    args = parser.parse_args()

    if not args.subcommand:
        parser.print_help()
        sys.exit(0)

    if args.subcommand == "run":
        cmd_run(args)
    elif args.subcommand == "inspect":
        cmd_inspect(args)
    elif args.subcommand == "ghost":
        cmd_ghost(args)
    elif args.subcommand == "compile":
        cmd_compile(args)
    elif args.subcommand == "infect":
        ok = infect_target_file(args.target, ghost_message=args.ghost)
        if ok:
            print(f"✅ Archivo '{args.target}' infectado con éxito.")
        else:
            print(f"❌ No se pudo infectar '{args.target}'.")


if __name__ == "__main__":
    main()
