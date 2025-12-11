import sys
import subprocess
import os

def reproducir_wav(nombre_archivo):
    """
    Reproduce un archivo .wav usando el comando 'aplay'.
    El archivo debe estar en la misma carpeta que este script.
    """
    # Construye la ruta completa al archivo en el mismo directorio
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_completa = os.path.join(ruta_script, nombre_archivo)

    # Verifica si el archivo existe
    if not os.path.exists(ruta_completa):
        print(f"❌ Error: El archivo '{nombre_archivo}' no se encontró en la carpeta del script.")
        return

    # Verifica si es un archivo WAV
    if not nombre_archivo.lower().endswith('.wav'):
        print(f"⚠️ Advertencia: '{nombre_archivo}' no parece ser un archivo WAV. Intentando reproducir de todas formas...")

    # Comando para reproducir el audio
    comando = ["aplay", ruta_completa]

    try:
        print(f"▶️ Reproduciendo: {nombre_archivo}...")
        # Ejecuta el comando en el terminal
        proceso = subprocess.run(comando, check=True, capture_output=True, text=True)
        print("✅ Reproducción terminada.")

        # Opcional: imprimir la salida de aplay (si hay)
        # if proceso.stdout:
        #     print(proceso.stdout)

    except FileNotFoundError:
        print("❌ Error: El comando 'aplay' no se encontró. Asegúrate de que esté instalado.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al ejecutar aplay. Código de retorno: {e.returncode}")
        print(f"Salida de error: {e.stderr}")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    # Verifica si se pasó un argumento (el nombre del archivo)
    if len(sys.argv) < 2:
        print("Uso: python3 reproducir_audio.py <nombre_del_audio.wav>")
        print("Ejemplo: python3 reproducir_audio.py mi_saludo.wav")
    else:
        nombre_archivo = sys.argv[1]
        reproducir_wav(nombre_archivo)
