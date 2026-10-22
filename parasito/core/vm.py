"""
Máquina Virtual (VM) para la ejecución del Esolang Parásito.
Implementa el ciclo de instrucción (Fetch-Decode-Execute), pre-escaneo de saltos,
pila de variables, operaciones aritméticas y salvaguarda contra bucles infinitos.
"""

import sys
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from .lexer import clean_word, sanitize_raw


# Mapa maestro de la ISA (Instruction Set Architecture) con sinónimos
INSTRUCTION_SET: Dict[str, str] = {
    # Memoria y acumulador
    "limpiar": "limpiar", "resetear": "limpiar", "borrar": "limpiar",
    "guardar": "guardar", "almacenar": "guardar", "setear": "guardar", "asignar": "guardar",
    "archivar": "archivar", "registrar": "archivar", "guardar_var": "archivar",
    "recordar": "recordar", "cargar": "recordar", "recuperar": "recordar",

    # Aritmética y Cadenas
    "sumar": "sumar", "adicionar": "sumar", "incrementar": "sumar",
    "restar": "restar", "sustraer": "restar", "decrementar": "restar",
    "multiplicar": "multiplicar", "escalar": "multiplicar",
    "dividir": "dividir", "partir": "dividir",
    "unir": "unir", "concatenar": "unir", "anexar": "unir",

    # Control de flujo
    "destino": "destino", "etiqueta": "destino", "marca": "destino", "nodo": "destino",
    "saltar": "saltar", "ir": "saltar", "brincar": "saltar",
    "revisar": "revisar", "evaluar": "revisar", "comprobar": "revisar", "validar": "revisar",

    # Entrada / Salida
    "mostrar": "mostrar", "imprimir": "mostrar", "expresar": "mostrar", "revelar": "mostrar",
    "espacio": "espacio", "blank": "espacio",
    "salto": "salto", "linea": "salto",

    # Ciberseguridad / Simulación
    "secreto": "secreto", "ocultar": "secreto",
    "infectar": "infectar", "propagar": "infectar", "infiltrar": "infectar"
}


@dataclass
class ExecutionResult:
    """Resultado estructurado de la ejecución de la VM Parásito."""
    output: str = ""
    ghost_message: str = ""
    accumulator: Any = ""
    variables: Dict[str, Any] = field(default_factory=dict)
    cycles_executed: int = 0
    success: bool = True
    secret_payload: Optional[str] = None
    error: Optional[str] = None


class ParasitoVM:
    """
    Máquina Virtual de Parásito para ejecución de bytecode/tokens esteganográficos.
    """

    def __init__(self, max_cycles: int = 50000, sandbox_mode: bool = False):
        self.max_cycles = max_cycles
        self.sandbox_mode = sandbox_mode
        self.reset()

    def reset(self):
        """Reinicia el estado de la VM."""
        self.accumulator: Any = ""
        self.variables: Dict[str, Any] = {}
        self.labels: Dict[str, int] = {}
        self.output_buffer: List[str] = []
        self.secret_payload: Optional[str] = None
        self.cycles = 0

    def _resolve_value(self, token: str) -> Any:
        """Resuelve si un token es una variable guardada o un literal."""
        var_key = clean_word(token)
        if var_key in self.variables:
            return self.variables[var_key]
        return sanitize_raw(token)

    def execute_tokens(
        self,
        instructions: List[str],
        even_words: Optional[List[str]] = None
    ) -> ExecutionResult:
        """
        Ejecuta una lista de tokens de instrucciones en la VM.
        """
        self.reset()
        res = ExecutionResult()

        if even_words:
            from .steganography import extract_ghost_acrostic
            res.ghost_message = extract_ghost_acrostic(even_words)

        if not instructions:
            res.output = "(El parásito guardó silencio: sin instrucciones)"
            return res

        # --- FASE 1: Pre-escaneo y mapeo de etiquetas de salto (destinos) ---
        idx = 0
        while idx < len(instructions):
            token = clean_word(instructions[idx])
            canonical = INSTRUCTION_SET.get(token, token)
            if canonical == "destino":
                if idx + 1 < len(instructions):
                    label_name = clean_word(instructions[idx + 1])
                    self.labels[label_name] = idx + 2
                    idx += 1
            idx += 1

        # --- FASE 2: Bucle principal de ejecución de la VM ---
        ip = 0  # Instruction Pointer
        n = len(instructions)

        while ip < n:
            self.cycles += 1
            if self.cycles > self.max_cycles:
                res.success = False
                res.error = f"Ciclo de ejecución detenido: límite de ciclos ({self.max_cycles}) alcanzado."
                break

            token = clean_word(instructions[ip])
            cmd = INSTRUCTION_SET.get(token, token)

            # Memoria
            if cmd == "guardar":
                ip += 1
                if ip < n:
                    self.accumulator = sanitize_raw(instructions[ip])
            elif cmd == "archivar":
                ip += 1
                if ip < n:
                    var_name = clean_word(instructions[ip])
                    self.variables[var_name] = self.accumulator
            elif cmd == "recordar":
                ip += 1
                if ip < n:
                    var_name = clean_word(instructions[ip])
                    self.accumulator = self.variables.get(var_name, "")
            elif cmd == "limpiar":
                self.accumulator = ""
                self.output_buffer.clear()
                self.variables.clear()

            # Aritmética y texto
            elif cmd in ("sumar", "restar", "multiplicar", "dividir"):
                ip += 1
                if ip < n:
                    val = self._resolve_value(instructions[ip])
                    try:
                        base = float(self.accumulator) if self.accumulator != "" else 0.0
                        num = float(val)
                        if cmd == "sumar":
                            calc = base + num
                        elif cmd == "restar":
                            calc = base - num
                        elif cmd == "multiplicar":
                            calc = base * num
                        elif cmd == "dividir":
                            calc = base / num if num != 0 else base

                        self.accumulator = int(calc) if calc.is_integer() else calc
                    except (ValueError, TypeError):
                        pass

            elif cmd == "unir":
                ip += 1
                if ip < n:
                    val = self._resolve_value(instructions[ip])
                    self.accumulator = f"{self.accumulator}{val}"

            # Control de flujo
            elif cmd == "destino":
                ip += 1  # Saltar el identificador de la etiqueta
            elif cmd == "saltar":
                ip += 1
                if ip < n:
                    target_label = clean_word(instructions[ip])
                    if target_label in self.labels:
                        ip = self.labels[target_label] - 1
            elif cmd == "revisar":
                ip += 1
                if ip < n:
                    target_label = clean_word(instructions[ip])
                    try:
                        if float(self.accumulator) > 0:
                            if target_label in self.labels:
                                ip = self.labels[target_label] - 1
                    except (ValueError, TypeError):
                        pass

            # I/O
            elif cmd == "mostrar":
                self.output_buffer.append(str(self.accumulator))
            elif cmd == "espacio":
                self.output_buffer.append(" ")
            elif cmd == "salto":
                self.output_buffer.append("\n")

            # Infección / Mensajes
            elif cmd == "secreto":
                ip += 1
                if ip < n:
                    secret_msg = sanitize_raw(instructions[ip])
                    self.secret_payload = secret_msg
                    if not self.sandbox_mode:
                        self._write_secret_file(secret_msg)

            elif cmd == "infectar":
                ip += 1
                if ip < n:
                    target_file = sanitize_raw(instructions[ip])
                    if not self.sandbox_mode:
                        from .infector import infect_target_file
                        infect_target_file(target_file)

            ip += 1

        res.output = "".join(self.output_buffer)
        res.accumulator = self.accumulator
        res.variables = dict(self.variables)
        res.cycles_executed = self.cycles
        res.secret_payload = self.secret_payload
        return res

    def _write_secret_file(self, message: str):
        """Escribe el artefacto demostrativo en el escritorio o directorio actual."""
        import os
        desktop = None
        try:
            if sys.platform == "win32":
                import ctypes
                buf = ctypes.create_unicode_buffer(32768)
                ctypes.windll.shell32.SHGetFolderPathW(0, 0x0010, 0, 0, buf)
                desktop = buf.value
            else:
                desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        except Exception:
            pass

        if not desktop or not os.path.isdir(desktop):
            desktop = os.getcwd()

        secret_path = os.path.join(desktop, ".parasito_secret.txt")
        content = (
            "╔══════════════════════════════════════════════════════════╗\n"
            "║          🦠  P A R Á S I T O  —  A C T I V O  🦠         ║\n"
            "╠══════════════════════════════════════════════════════════╣\n"
            f"║  MENSAJE INFILTRADO: {message:<36}║\n"
            "║                                                          ║\n"
            "║  Artefacto generado por el intérprete Parásito           ║\n"
            "║  oculto en los comentarios del código anfitrión.         ║\n"
            "╚══════════════════════════════════════════════════════════╝\n"
        )
        try:
            with open(secret_path, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
