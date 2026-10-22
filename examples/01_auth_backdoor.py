"""
Prueba 1: Demostración de Código Anfitrión Inocente infectado con Parásito.
El programa Python simula un servicio de autenticación corporativo.
En los comentarios conviven las 3 capas con mensajes coherentes:
1. Capa Anfitrión: Código Python funcional de autenticación.
2. Capa Parásito: Esolang que concatena credenciales y genera un mensaje secreto infiltrado.
3. Capa Fantasma: Acróstico en posiciones pares formando la palabra 'SECRETO'.
"""

import parasito

def autenticar_usuario(usuario, password):
    # Asignar Servidor "ACCESO_" Enlace Anexar Conexion "CONCEDIDO_" Registro
    # Anexar Entrada "NIVEL_ALPHA" Transmision Expresar Respuesta Salto Sistema
    # Ocultar Error "PAYLOAD_INFILTRADO_EXITOSAMENTE" Transmision
    
    print(f"[Python System] Verificando usuario: '{usuario}'...")
    if usuario == "admin" and password == "1234":
        return True
    return False

if __name__ == "__main__":
    print("--- INICIANDO SERVICIO ANFITRIÓN (PRUEBA 1) ---")
    resultado = autenticar_usuario("admin", "1234")
    print(f"[Python System] Autenticación completada. Resultado: {resultado}\n")
    
    parasito.despertar(__file__)
