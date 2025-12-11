import sys
import os
try:
    import simpleaudio as sa
except ImportError:
    print("❌ Error: La biblioteca 'simpleaudio' no está instalada. Ejecuta 'pip install simpleaudio'.")
    sys.exit(1)

def reproducir_wav_sa(nombre_archivo):
    """
    Reproduce un archivo .wav usando la biblioteca simpleaudio.
    El archivo debe estar en la misma carpeta que este script.
    """
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_completa = os.path.join(ruta_script, nombre_archivo)

    if not os.path.exists(ruta_completa):
        print(f"❌ Error: El archivo '{nombre_archivo}' no se encontró.")
        return

    try:
        print(f"▶️ Reproduciendo: {nombre_archivo}...")
        wave_obj = sa.WaveObject.from_wave_file(ruta_completa)
        play_obj = wave_obj.play()
        # Espera a que la reproducción termine
        play_obj.wait_done()
        print("✅ Reproducción terminada.")

    except Exception as e:
        print(f"❌ Ocurrió un error al reproducir el audio: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 reproducir_audio_sa.py <nombre_del_audio.wav>")
    else:
        nombre_archivo = sys.argv[1]
        reproducir_wav_sa(nombre_archivo)
