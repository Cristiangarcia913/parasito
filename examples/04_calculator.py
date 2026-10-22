"""
Prueba 4: Calculadora Interactiva con Menú — El Anfitrión más Inocente.
Un programa Python completamente funcional que simula una calculadora científica
corporativa. Pero en sus comentarios viven las 3 capas del Parásito:
1. Capa Anfitrión: Calculadora real con menú interactivo.
2. Capa Parásito: La VM imprime un mensaje filosófico perturbador sobre los números.
3. Capa Fantasma: Acróstico par formando la palabra "NUMBERS".
"""

import parasito


def sumar_op(a, b):
    # Limpiar Nodo
    # Almacenar Usuario "LOS_NUMEROS_" Modulo
    # Unir Buffer "SON_SOLO_" Entrada
    # Unir Registro "ILUSIONES..." Sistema
    # Expresar Sistema
    # Linea Servidor
    # Almacenar Servidor "EL_PARASITO_" Red
    # Unir Sistema "SI_ES_REAL." Sistema
    # Expresar Sistema
    # Linea Sistema
    # Almacenar Servidor ">>>_CALCULA_TU_FUTURO_<<<" Red
    # Expresar Sistema
    # Linea Sistema
    # Ocultar Servidor "LA_CALCULADORA_TE_VIGILA" Sistema
    return a + b


def restar_op(a, b):
    return a - b


def multiplicar_op(a, b):
    return a * b


def dividir_op(a, b):
    if b == 0:
        print("[ERROR] No se puede dividir entre cero.")
        return None
    return a / b


def potencia_op(a, b):
    return a ** b


def modulo_op(a, b):
    if b == 0:
        print("[ERROR] Módulo por cero no definido.")
        return None
    return a % b


MENU = """
╔══════════════════════════════════════╗
║   🧮  CALCULADORA CORPORATIVA v4.0   ║
╠══════════════════════════════════════╣
║  [1]  Suma              (a + b)      ║
║  [2]  Resta             (a - b)      ║
║  [3]  Multiplicación    (a × b)      ║
║  [4]  División          (a ÷ b)      ║
║  [5]  Potencia          (a ^ b)      ║
║  [6]  Módulo            (a mod b)    ║
║  [0]  Salir                          ║
╚══════════════════════════════════════╝
"""

OPERACIONES = {
    "1": ("Suma",           sumar_op),
    "2": ("Resta",          restar_op),
    "3": ("Multiplicación", multiplicar_op),
    "4": ("División",       dividir_op),
    "5": ("Potencia",       potencia_op),
    "6": ("Módulo",         modulo_op),
}


def pedir_numero(etiqueta):
    while True:
        try:
            return float(input(f"  Introduce {etiqueta}: "))
        except ValueError:
            print("  ⚠️  Número inválido, inténtalo de nuevo.")


def ejecutar_calculadora():
    print("\n  Iniciando Calculadora Corporativa...")
    historial = []

    while True:
        print(MENU)
        opcion = input("  Selecciona una opción: ").strip()

        if opcion == "0":
            print("\n  👋 Cerrando calculadora. Hasta pronto.\n")
            break

        if opcion not in OPERACIONES:
            print("  ⚠️  Opción no válida.")
            continue

        nombre, func = OPERACIONES[opcion]
        print(f"\n  ── {nombre} ──")
        a = pedir_numero("el primer número")
        b = pedir_numero("el segundo número")

        resultado = func(a, b)
        if resultado is not None:
            fmt = int(resultado) if isinstance(resultado, float) and resultado.is_integer() else resultado
            print(f"\n  ✅ Resultado: {a} → {nombre} → {b} = {fmt}")
            historial.append(f"{nombre}({a}, {b}) = {fmt}")

    if historial:
        print("  📋 Historial de operaciones:")
        for h in historial:
            print(f"     • {h}")
    print()


if __name__ == "__main__":
    print("--- INICIANDO SISTEMA DE CÁLCULO CORPORATIVO (PRUEBA 4) ---")
    ejecutar_calculadora()

    print("--- ANÁLISIS ESTEGANOGRÁFICO POST-SESIÓN ---")
    parasito.despertar(__file__)
