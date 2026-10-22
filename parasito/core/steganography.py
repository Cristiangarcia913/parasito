"""
Módulo de Esteganografía y Capa Fantasma de Parásito.
Gestiona el análisis, extracción y síntesis de acrósticos ocultos
utilizando vocabulario técnico coherente en las palabras pares.
"""

from typing import List, Dict
from .lexer import sanitize_raw, clean_word, tokenize_comment_text

# Diccionario enriquecido de palabras pares técnicas organizadas por su letra inicial
DICCIONARIO_PEGAMENTOS: Dict[str, List[str]] = {
    'A': ["acceso", "archivo", "almacenamiento", "analisis", "auditoria", "activo", "algoritmo", "api"],
    'B': ["bloque", "buffer", "bus", "base", "bucle", "binario", "balancin", "banco"],
    'C': ["codigo", "conexion", "control", "cliente", "consulta", "carga", "cifrado", "ciclo"],
    'D': ["datos", "direccion", "depuracion", "disco", "demonio", "destino", "dispositivo", "driver"],
    'E': ["entrada", "estructura", "ejecucion", "evento", "estado", "enlace", "error", "esquema"],
    'F': ["funcion", "flujo", "fichero", "formato", "filtro", "firma", "fragmento", "fuente"],
    'G': ["gestion", "garantia", "generacion", "grupo", "gestor", "grafico", "guardia", "gateway"],
    'H': ["hilo", "historial", "herramienta", "huella", "hardware", "host", "hash", "header"],
    'I': ["interfaz", "instruccion", "informe", "indice", "inicio", "identificador", "inyeccion", "imagen"],
    'J': ["jerarquia", "jornada", "junta", "juicio", "job"],
    'K': ["kernel", "key", "keystore"],
    'L': ["libreria", "logica", "lectura", "llamada", "linea", "lote", "limite", "listado"],
    'M': ["memoria", "modulo", "mensaje", "matriz", "marco", "monitor", "metodo", "malla"],
    'N': ["nodo", "nivel", "nucleo", "norma", "nota", "numero", "nube", "negociacion"],
    'O': ["operacion", "objeto", "orden", "origen", "optimizacion", "salida", "observador"],
    'P': ["proceso", "paquete", "puerto", "parametro", "pila", "protocolo", "parche", "payload"],
    'Q': ["quorum", "quiebre", "queue", "query"],
    'R': ["registro", "red", "respuesta", "rutina", "ruta", "recurso", "rastreo", "reserva"],
    'S': ["sistema", "servidor", "salida", "sesion", "socket", "subred", "secuencia", "seguridad"],
    'T': ["trama", "tabla", "tipo", "traza", "tarea", "tiempo", "transmision", "terminal"],
    'U': ["usuario", "unidad", "ubicacion", "utilidad", "urgencia", "uuid"],
    'V': ["variable", "valor", "ventana", "verificacion", "vector", "volumen", "version"],
    'W': ["web", "worker", "workflow"],
    'X': ["xml", "xdr", "x509"],
    'Y': ["yarda", "yaml"],
    'Z': ["zona", "zip", "zero"]
}


def extract_ghost_acrostic(even_words: List[str]) -> str:
    """
    Extrae el mensaje oculto (acróstico) leyendo la primera letra
    de cada una de las palabras pares.
    """
    acrostico = []
    for word in even_words:
        cleaned = sanitize_raw(word)
        if cleaned:
            # Extraer primer carácter alfanumérico
            for ch in cleaned:
                if ch.isalnum():
                    acrostico.append(ch.upper())
                    break
    return "".join(acrostico)


def synthesize_steganographic_comment(
    executable_instructions: List[str],
    ghost_secret_message: str
) -> str:
    """
    Sintetiza un comentario técnico coherente entrelazando:
    - Las palabras impares (instrucciones ejecutables de la VM)
    - Las palabras pares (pegamento gramatical cuyas iniciales forman el acróstico deseado)
    """
    ghost_chars = [c.upper() for c in ghost_secret_message if c.isalnum()]
    line = []
    idx_ghost = 0

    for i, instruction in enumerate(executable_instructions):
        line.append(instruction)

        if idx_ghost < len(ghost_chars):
            target_char = ghost_chars[idx_ghost]
            idx_ghost += 1
            candidates = DICCIONARIO_PEGAMENTOS.get(target_char, ["sistema"])
            glue_word = candidates[i % len(candidates)]
        else:
            # Pegamento neutral si ya se completó el acróstico
            default_candidates = DICCIONARIO_PEGAMENTOS['S']
            glue_word = default_candidates[i % len(default_candidates)]

        line.append(glue_word)

    return " ".join(line)
