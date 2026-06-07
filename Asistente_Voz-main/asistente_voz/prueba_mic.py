import speech_recognition as sr

def probar_microfono():
    r = sr.Recognizer()
    # Listar micrófonos disponibles para confirmar
    print("Micrófonos detectados:")
    for i, nombre in enumerate(sr.Microphone.list_microphone_names()):
        print(f"[{i}] {nombre}")
        
    print("\nIniciando prueba. Por favor, habla ahora (tienes 5 segundos)...")
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            
        print("Procesando audio con Google...")
        texto = r.recognize_google(audio, language="es-MX")  # type: ignore[attr-defined]
        print(f"\n¡Éxito! Escuché: '{texto}'")
    except sr.WaitTimeoutError:
        print("\nError: Se acabó el tiempo. No se detectó sonido.")
    except sr.UnknownValueError:
        print("\nError: El micrófono capturó audio, pero no entendí lo que dijiste.")
    except Exception as e:
        print(f"\nError general: {e}")

if __name__ == "__main__":
    probar_microfono()