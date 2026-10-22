# 🦠 Parásito — El Lenguaje de Programación Esteganográfico
### Steganographic Esoteric Programming Language (Esolang) & Covert VM Engine

[![Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0%20(Pure%20Stdlib)-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Category](https://img.shields.io/badge/category-Esolang%20%26%20Cybersecurity-red.svg)]()
[![Author](https://img.shields.io/badge/author-Cristian%20Garc%C3%ADa-black.svg)](https://github.com/Cristiangarcia913)

> *"El código que ves hace una cosa; los comentarios que ignoras hacen otra, y el ruido blanco esconde un grito de auxilio."*

**Parásito** es un lenguaje de programación esotérico (**esolang**) y motor de ejecución encubierta (*covert execution*) que no posee archivos fuente propios: **vive como un organismo parásito dentro de los comentarios de un programa anfitrión en Python**.

Mientras el intérprete de Python ejecuta el programa funcional principal ignorando por completo los comentarios, **la Máquina Virtual de Parásito ignora el código Python y compila exclusivamente los comentarios**, ejecutando una lógica independiente y extrayendo un mensaje acróstico invisible.

---

## 📌 Tabla de Contenidos
- [Concepto: La Regla de la Imparidad](#-concepto-la-regla-de-la-imparidad)
- [Las 3 Capas Superpuestas](#-las-3-capas-superpuestas)
- [Arquitectura de la Máquina Virtual](#-arquitectura-de-la-máquina-virtual)
- [Tabla de Instrucciones (ISA)](#-tabla-de-instrucciones-isa)
- [Instalación y Configuración](#-instalación-y-configuración)
- [Uso del CLI](#-uso-del-cli)
- [Demos Incluidas](#-demos-incluidas)
- [Relevancia en Ciberseguridad y Red Teaming](#-relevancia-en-ciberseguridad-y-red-teaming)
- [Tests Automatizados](#-tests-automatizados)
- [Autor](#-autor)
- [Licencia](#-licencia)

---

## 🧠 Concepto: La Regla de la Imparidad

Para un auditor o un analizador estático (SAST), los comentarios del código fuente parecen texto técnico ordinario sobre arquitectura y servidores. Sin embargo, Parásito aplica una regla estricta de división léxica basada en la paridad de posición:

- **Palabras en posición IMPAR (1ª, 3ª, 5ª...)** ➔ Son las **instrucciones ejecutables** de la VM Parásito (opcodes, operandos, etiquetas).
- **Palabras en posición PAR (2ª, 4ª, 6ª...)** ➔ Son **pegamento gramatical** técnico invisible para la VM, pero su **primera letra** compone un acróstico secreto para el ojo humano (**Capa Fantasma**).

### Ejemplo Diseccionado

```text
# Limpiar Nodo  Almacenar Usuario  "LOS_NUMEROS_" Modulo  Unir Buffer  "SON_SOLO_" Entrada
  ───────────────────────────────────────────────────────────────────────────────────────
  Impar:  Limpiar    Almacenar        "LOS_NUMEROS_"         Unir          "SON_SOLO_"
  Par:            Nodo        Usuario                Modulo       Buffer              Entrada
                  N           U                      M            B                   E  ➔ N·U·M·B·E…
```

1. **Python:** Ignora la línea (es un comentario estándar `#`).
2. **VM Parásito:** Ejecuta el bytecode: `limpiar`, `guardar "LOS_NUMEROS_"`, `unir "SON_SOLO_"`.
3. **Capa Fantasma:** La primera letra de las palabras pares deletrea: **`NUMBERS`**.

---

## 📑 Las 3 Capas Superpuestas

| Capa | Entorno de Ejecución | Visibilidad | Función |
|---|---|---|---|
| **Capa 1 — Anfitrión** | Intérprete Python | Código funcional | Sistema de login, calculadora, microservicio corporativo. |
| **Capa 2 — Parásito** | VM Parásito | Bytecode en posiciones impares | Aritmética, memoria, bucles, inyección de payloads. |
| **Capa 3 — Fantasma** | Ojo humano / Escáner | Acróstico en posiciones pares | Mensaje esteganográfico de control o exfiltración. |

---

## 🛠️ Arquitectura de la Máquina Virtual

```text
Código Anfitrión (.py)
         │
         ├── [1] tokenize: Extracción léxica de bloques de comentarios
         │
         ├── [2] Lexer: Separación de Impares (VM) y Pares (Fantasma)
         │
         ├── [3] Fase 1 (Pre-Scan): Resolución y mapeo de etiquetas de salto ('destino')
         │
         ├── [4] Fase 2 (Execution Loop):
         │         ├── Acumulador & Variables
         │         ├── Operaciones Aritméticas (+, -, *, /) y Cadenas ('unir')
         │         ├── Control de Flujo ('saltar', 'revisar') con protección anti-bucle
         │         └── I/O & Inyección
         │
         └── [5] Fase 3 (Acróstico): Reconstrucción del mensaje de la Capa Fantasma
```

---

## 📖 Tabla de Instrucciones (ISA)

| Categoría | Comando Principal | Sinónimos Válidos | Operación |
|---|---|---|---|
| **MEM** | `limpiar` | `resetear`, `borrar` | Resetea acumulador, memoria y buffer de salida |
| **MEM** | `guardar <val>` | `almacenar`, `setear`, `asignar` | Carga un valor literal o número en el acumulador |
| **MEM** | `archivar <var>` | `registrar`, `guardar_var` | Guarda el contenido del acumulador en la variable `<var>` |
| **MEM** | `recordar <var>` | `cargar`, `recuperar` | Carga el valor de `<var>` en el acumulador |
| **ARITH** | `sumar <val>` | `adicionar`, `incrementar` | `Acumulador ← Acumulador + val` |
| **ARITH** | `restar <val>` | `sustraer`, `decrementar` | `Acumulador ← Acumulador − val` |
| **ARITH** | `multiplicar <val>` | `escalar` | `Acumulador ← Acumulador × val` |
| **ARITH** | `dividir <val>` | `partir` | `Acumulador ← Acumulador ÷ val` (seguro contra ÷0) |
| **ARITH** | `unir <val>` | `concatenar`, `anexar` | Concatenación de cadenas |
| **FLOW** | `destino <id>` | `etiqueta`, `marca`, `nodo` | Declara una etiqueta de salto |
| **FLOW** | `saltar <id>` | `ir`, `brincar` | Salto incondicional al destino `<id>` |
| **FLOW** | `revisar <id>` | `evaluar`, `comprobar`, `validar` | Salto condicional si `Acumulador > 0` |
| **I/O** | `mostrar` | `imprimir`, `expresar`, `revelar` | Envía el acumulador al buffer de salida |
| **I/O** | `espacio` | `blank` | Inserta un espacio `" "` |
| **I/O** | `salto` | `linea` | Inserta un salto de línea `\n` |
| **INF** | `secreto <msg>` | `ocultar` | Genera el artefacto demostrativo `.parasito_secret.txt` |
| **INF** | `infectar <ruta>` | `propagar`, `infiltrar` | Inyecta código Parásito en el archivo objetivo |

---

## 📦 Instalación y Configuración

Parásito está implementado en **Python puro con cero dependencias externas** (utiliza únicamente la biblioteca estándar).

```bash
git clone https://github.com/Cristiangarcia913/parasito.git
cd parasito
pip install -e .
```

---

## 💻 Uso del CLI

El paquete proporciona el comando global `parasito`:

### 1. Ejecutar el código Parásito de un archivo
```bash
parasito run examples/01_auth_backdoor.py
```

### 2. Modo Sandbox (sin escribir artefactos en disco)
```bash
parasito run examples/03_turing_loop.py --sandbox
```

### 3. Diseccionar las 3 capas del archivo
```bash
parasito inspect examples/04_calculator.py
```

### 4. Extraer únicamente el Acróstico Fantasma
```bash
parasito ghost examples/01_auth_backdoor.py
# Salida: SECRET
```

### 5. Sintetizador de comentarios esteganográficos
Genera una línea técnica coherente con el código y acróstico que desees:
```bash
parasito compile -i "limpiar guardar 42 archivar token mostrar" -g "ROOT"
# Salida: # limpiar Red guardar Origen 42 Operacion archivar Trama token Tarea mostrar Tipo
```

---

## 🧪 Demos Incluidas

En el directorio [`examples/`](examples/) se incluyen demostraciones funcionales completas:

1. **[`01_auth_backdoor.py`](examples/01_auth_backdoor.py)**: Simula un sistema de login empresarial. En los comentarios, Parásito concatena credenciales elevadas y el acróstico revela **`SECRET`**.
2. **[`02_supply_chain.py`](examples/02_supply_chain.py)**: Simula una inyección esteganográfica en librerías de terceros (Acróstico: **`HACKED`**).
3. **[`03_turing_loop.py`](examples/03_turing_loop.py)**: Demostración de Turing-completitud con un bucle de cuenta regresiva condicional y manejo de variables (Acróstico: **`CICLO`**).
4. **[`04_calculator.py`](examples/04_calculator.py)**: Calculadora corporativa interactiva con menú. Al operar, la VM construye un mensaje paralelo y revela el acróstico **`NUMBERS`**.
5. **[`05_network_core.py`](examples/05_network_core.py)**: Demostración compacta de control de flujo en un servicio de red.

---

## 🛡️ Relevancia en Ciberseguridad y Red Teaming

Parásito no es solo una curiosidad matemática; ilustra vectores avanzados de evasión y esteganografía de código:

- **Bypass de SAST (Static Application Security Testing):** Los escáneres estáticos de vulnerabilidades descartan sistemáticamente los comentarios `#` al generar el AST (Abstract Syntax Tree).
- **Canales Encubiertos (Covert Channels):** Permite transportar cargas útiles o comandos C2 en repositorios públicos sin levantar alertas heurísticas.
- **Supply-Chain Polyglots:** Demuestra cómo un paquete open source puede lucir completamente inofensivo en auditorías superficiales mientras ejecuta lógica no documentada.

---

## 🔬 Tests Automatizados

La suite de pruebas unitarias cubre el lexer, la máquina virtual, las operaciones de control de flujo y la extracción esteganográfica:

```bash
python -m unittest discover -s tests -v
```

Resultado:
```text
test_demo_auth_ghost ... ok
test_demo_calculator_ghost ... ok
test_demo_turing_loop ... ok
test_clean_word ... ok
test_extract_comments ... ok
test_sanitize_raw ... ok
test_tokenize_quotes ... ok
test_extract_acrostic ... ok
test_synthesize_comment ... ok
test_arithmetic ... ok
test_loop ... ok
test_strings ... ok
test_variables ... ok

Ran 13 tests in 0.009s - OK
```

---

## 👤 Autor

- **Cristian García** ([@Cristiangarcia913](https://github.com/Cristiangarcia913))

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.
