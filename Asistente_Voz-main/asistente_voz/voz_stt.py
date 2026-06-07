"""
Módulo de Reconocimiento de Voz (STT) para el Asistente de Voz centauro

"""

import speech_recognition as sr

from asistente_voz.config import (
    LANGUAGE_STT,
    LISTEN_TIMEOUT_S,
    PHRASE_TIME_LIMIT_S,
    MIC_DEVICE_INDEX,
)


class ReconocimientoVoz:
    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()
        self._mic_index = MIC_DEVICE_INDEX
        with sr.Microphone(device_index=self._mic_index) as source:
            print("🎚️ Calibrando el ruido de fondo del entorno... por favor guarda silencio 2 segundos.")
            self.recognizer.adjust_for_ambient_noise(source, duration=2.0)
            print("✅ Micrófono calibrado y listo.")

        print(f"🎤 Usando micrófono índice: {self._mic_index if self._mic_index is not None else 'por defecto'}")

    def escuchar_audio(self) -> str:
        """Escucha con manejo seguro del micrófono."""
        try:
            # Creamos el micrófono de forma más segura
            mic = sr.Microphone(device_index=self._mic_index)
            
            with mic as source:
                print("🎚️ Ajustando ruido de fondo...")
                print("✅ Ruido calibrado.")

                print("👂 Escuchando... (Di 'centauro' + comando)")
                
                audio = self.recognizer.listen(
                    source,
                    timeout=LISTEN_TIMEOUT_S,
                    phrase_time_limit=PHRASE_TIME_LIMIT_S
                )

            print("⏳ Enviando a Google...")
            texto = self.recognizer.recognize_google(audio, language=LANGUAGE_STT)  # type: ignore[attr-defined]
            print(f"✅ Reconocido: {texto}")
            return texto.strip()

        except sr.WaitTimeoutError:
            print("⏰ Tiempo agotado. No se detectó voz.")
        except sr.UnknownValueError:
            print("❓ No se entendió el audio.")
        except sr.RequestError as e:
            print(f"❌ Error de Google: {e}")
        except Exception as e:
            print(f"⚠️ Error general del micrófono: {e}")
            print("   Intenta cambiar el MIC_DEVICE_INDEX en config.py")

        return ""