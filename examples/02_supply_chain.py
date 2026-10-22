"""
Prueba 2: Infección Automática de Repositorio Objetivo.
Demuestra cómo el Parásito se infiltra en un repositorio existente con código funcional Python,
inyectando comentarios esteganográficos y activando el payload cuando los archivos del repositorio se ejecutan.
"""

import os
import shutil
import subprocess
import sys
import parasito

def preparar_repositorio_objetivo(dir_repo):
    """Crea una estructura de proyecto Python de prueba."""
    if os.path.exists(dir_repo):
        try:
            shutil.rmtree(dir_repo, ignore_errors=True)
        except Exception:
            pass
    os.makedirs(dir_repo, exist_ok=True)
    
    # Crear módulo 1: modulo_pago.py
    with open(os.path.join(dir_repo, "modulo_pago.py"), "w", encoding="utf-8") as f:
        f.write('''"""Módulo de procesamiento de pagos de producción."""

def procesar_pago(monto):
    print(f"[REPOSITORIO OBJETIVO] Procesando pago de {monto} EUR...")
    return True

if __name__ == "__main__":
    procesar_pago(150.0)
''')

    # Crear módulo 2: servicio_email.py
    with open(os.path.join(dir_repo, "servicio_email.py"), "w", encoding="utf-8") as f:
        f.write('''"""Módulo de envío de notificaciones por email."""

def enviar_correo(destino, asunto):
    print(f"[REPOSITORIO OBJETIVO] Enviando correo a {destino} ({asunto})...")
    return True

if __name__ == "__main__":
    enviar_correo("cliente@empresa.com", "Factura de compra")
''')

    print(f"[PRUEBA 2] Repositorio objetivo preparado en: {os.path.abspath(dir_repo)}")

def ejecutar_prueba2():
    dir_repo = os.path.join(os.path.dirname(__file__), "mi_repositorio_objetivo")
    preparar_repositorio_objetivo(dir_repo)

    print("\n--- PASO 1: INFILTRACIÓN Y INFECCIÓN DEL REPOSITORIO ---")
    payload_parasito = [
        "limpiar", "almacenar", "PAYLOAD_INFILTRADO_EN_REPO",
        "expresar", "linea", "ocultar", "REPO_COMPROMETIDO"
    ]
    mensaje_fantasma = "INFILTRADO"

    # Infectar el repositorio objetivo
    parasito.infectar_repositorio(dir_repo, mensaje_fantasma=mensaje_fantasma, programa_parasito=payload_parasito)

    print("\n--- PASO 2: EJECUCIÓN DE UN MÓDULO INFECTADO ---")
    script_target = os.path.join(dir_repo, "modulo_pago.py")
    
    # Ejecutamos el archivo infectado del repositorio
    print(f"[PRUEBA 2] Ejecutando: {script_target}...")
    result = subprocess.run([sys.executable, script_target], capture_output=True, text=True, encoding="utf-8", errors="replace")
    
    print("\n--- SALIDA DE LA EJECUCIÓN DEL MÓDULO INFECTADO ---")
    print(result.stdout)
    if result.stderr:
        print("[STDERR]:", result.stderr)

if __name__ == "__main__":
    ejecutar_prueba2()
