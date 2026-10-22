"""
Punto de acceso y compatibilidad hacia atrás para Parásito Esolang.
Redirige al nuevo paquete modular profesional 'parasito'.

Autor: Cristian García (@Cristiangarcia913)
Versión: 2.0.0
"""

from parasito import (
    despertar,
    run_file,
    inspect_file,
    ParasitoVM,
    infect_target_file,
    infect_directory,
    __version__,
    __author__
)

# Alias para compatibilidad con código legado
infectar_archivo = infect_target_file
infectar_repositorio = infect_directory

if __name__ == "__main__":
    from parasito.cli import main
    main()
