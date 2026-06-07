# prueba de cambio del Asistente Centauro - Asistente de Voz por Comandos

Aplicación especializada en Python para el reconocimiento, procesamiento y ejecución de comandos de voz en lenguaje natural. El sistema valida las instrucciones mediante una gramática formal y ejecuta acciones específicas: búsquedas en web, reproducción de contenido multimedia, apertura de aplicaciones en Windows y generación de respuestas por síntesis de voz.

---

## Descripción General

**Asistente Centauro** constituye un sistema modular y extensible de procesamiento de comandos de voz. La arquitectura permite ampliar funcionalidades mediante la adición de nuevos verbos, reglas gramaticales y acciones sin modificar el núcleo del sistema.

El proyecto incluye dos componentes independientes:
- **Asistente de Voz**: Sistema principal de reconocimiento y ejecución de comandos
- **Sistema Experto de Animales**: Módulo de identificación basado en características (Base_Hechos.py)

---

## Composición del Sistema

### Estructura de Componentes

La aplicación se estructura en los siguientes módulos Python dentro del paquete `asistente_voz/`:

#### 1. **agente.py** — Orquestador Central
Componente principal que coordina el flujo de procesamiento. Implementa el ciclo de procesamiento:
- Captura de entrada (audio o texto)
- Invocación del motor de validación gramical
- Despacho de acciones según el verbo reconocido
- Generación de respuesta por síntesis de voz

#### 2. **config.py** — Centro de Configuración
Centraliza todos los parámetros del sistema:
- Palabras de activación (`WAKE_WORDS`): centauro, centauro, google, cortana
- Verbos reconocidos (`VERBOS`): reproduce, busca, abre
- Rutas de aplicaciones en Windows (Edge, Notepad, Word)
- Parámetros de reconocimiento de voz (idioma, timeouts)
- Parámetros de síntesis de voz (velocidad, volumen, motor)
- Índice del dispositivo de micrófono

#### 3. **gramatica.py** — Validador de Sintaxis
Define la gramática formal (CFG - Context-Free Grammar) usando NLTK. Especifica:
- Estructura válida de órdenes: [palabra_activación] [verbo] [complemento]
- Patrones para comandos abiertos (búsquedas)
- Patrones para comandos cerrados (apertura de aplicaciones)
- Comodines para objetos indefinidos

#### 4. **voz_stt.py** — Motor de Entrada (Speech-To-Text)
Módulo de captura de audio y conversión a texto:
- Captura mediante PyAudio del dispositivo de micrófono
- Calibración automática de ruido de fondo
- Envío a Google Cloud Speech Recognition API
- Manejo de excepciones y timeouts

#### 5. **voz_tts.py** — Motor de Salida (Text-To-Speech)
Módulo de síntesis de voz:
- En Windows: utiliza SAPI mediante win32com (pywin32)
- Alternativa: pyttsx3 con motor sapi5
- Configuración de velocidad y volumen
- Selección de idioma (español, inglés u otro según SO)

#### 6. **texto.py** — Normalizador de Texto
Preprocesamiento de cadenas de entrada:
- Conversión a minúsculas
- Eliminación de acentos y caracteres especiales
- Tokenización en palabras
- Reorden de tokens si es necesario (corrección de orden verbo-activación)

#### 7. **acciones.py** — Ejecutor de Tareas
Implementación de funciones específicas:
- `reproducir(query)`: Abre búsqueda en YouTube vía pywhatkit
- `buscar(query)`: Abre búsqueda en Google vía pywhatkit
- `abrir_app(nombre)`: Lanza aplicaciones Windows mediante subprocess
- Extensible para nuevas acciones

#### 8. **Base_Hechos.py** — Base de Conocimientos
Sistema experto independiente con base de hechos:
- Diccionario de 40+ animales
- Rasgos característicos de cada especie
- Integrable como módulo dentro del asistente

### Punto de Entrada

- **Asistente_Voz_IA.py**: Ejecutable principal que carga e inicia el agente

---

## Requisitos del Sistema

### Requisitos Técnicos Mínimos

| Requisito | Especificación |
|-----------|--------------|
| **Sistema Operativo** | Windows 10/11 (recomendado) |
| **Versión de Python** | 3.10 o superior |
| **Conexión a Internet** | Requerida para Google Speech Recognition |
| **Dispositivo de Audio** | Micrófono (opcional: modo texto sin micrófono) |
| **Memoria RAM** | 512 MB mínimo |
| **Espacio en Disco** | 100 MB para entorno virtual + dependencias |

### Dependencias de Software

```
nltk>=3.8.1              # Gramática formal y análisis sintáctico
pyttsx3>=2.90            # Síntesis de voz (alternativa/fallback)
SpeechRecognition>=3.10.0 # Reconocimiento de voz
pywhatkit>=5.0           # Integración con navegador para búsquedas
pyaudio>=0.2.14          # Captura de audio del micrófono
```

### Requisitos Opcionales (Recomendados)

```
pywin32                  # Acceso a SAPI para mejor síntesis en Windows
```

### Requisitos de Configuración

Antes de ejecutar, deben definirse en `asistente_voz/config.py`:
- Índice del micrófono (si es diferente al dispositivo por defecto)
- Rutas de aplicaciones Windows (Edge, Notepad, Word)
- Idioma de reconocimiento (es-MX, es-ES, en-US, etc.)
- Parámetros de velocidad y volumen de síntesis

---

## Virtudes y Características Principales

### 1. Arquitectura Modular
- Cada componente (STT, TTS, gramática, acciones) existe de forma independiente
- Permite reemplazar o mejorar componentes sin afectar el resto
- Facilita pruebas unitarias de cada módulo

### 2. Extensibilidad Facilitada
- Agregar nuevos verbos requiere solo editar `config.py` y `gramatica.py`
- Nuevas acciones se implementan en `acciones.py` sin tocar el orquestador
- Sistema diseñado para crecimiento sin refactorización masiva

### 3. Validación Gramical Rigurosa
- Utiliza Context-Free Grammar (CFG) formal, no simple análisis de palabras clave
- Rechaza frases mal formadas antes de intentar ejecutarlas
- Evita errores de ejecución por malinterpretación

### 4. Soporte Multiidioma
- Configuración flexible de idioma para reconocimiento
- Síntesis de voz adaptable al idioma del SO
- Normalización de acentos y caracteres especiales

### 5. Múltiples Modos de Operación
- **Modo voz**: Entrada por micrófono, salida por altavoz
- **Modo texto**: Entrada por consola (sin necesidad de micrófono)
- **Modo debug**: Imprime información de cada etapa del procesamiento

### 6. Documentación y Comentarios Extensos
- Código fuente comentado íntegramente en español
- Archivos de configuración con explicaciones detalladas
- Ejemplos de uso en cada módulo

### 7. Integración con Servicios Web
- YouTube: Búsqueda y reproducción de contenido
- Google: Búsqueda web general
- Navegador del SO: Manejo automático de URLs

### 8. Sistema de Respuestas Verbales
- Confirmación de acciones mediante síntesis de voz
- Mensajes de error claramente comunicados
- Guía de usuario integrada por voz

### 9. Componente de Sistema Experto
- Base de conocimientos con características de +60 animales
- Identificación por rasgos independiente del asistente de voz
- Potencial de integración para expansión de inteligencia

### 10. Configuración Sin Código
- Variables de entorno para ajustes sin editar archivos
- Parámetros centralizados en un único archivo de configuración
- Permite experimentación rápida

---

## Flujo de Procesamiento

### Ciclo Estándar de Ejecución

```
┌─────────────────────────────────┐
│ 1. CAPTURA DE ENTRADA           │
│ - Audio del micrófono (STT)     │
│ - O línea de texto (consola)    │
└──────────────┬──────────────────┘
               │
               ↓
┌─────────────────────────────────┐
│ 2. NORMALIZACIÓN                │
│ - Minúsculas                    │
│ - Eliminación de acentos        │
│ - Tokenización                  │
│ - Reorden si es necesario       │
└──────────────┬──────────────────┘
               │
               ↓
┌─────────────────────────────────┐
│ 3. VALIDACIÓN GRAMATICAL        │
│ - Análisis CFG                  │
│ - Extracción de verbo           │
│ - Extracción de complemento     │
└──────────────┬──────────────────┘
               │
         ¿Válida?
        /       \
      SÍ         NO
     /             \
    │               │
    ↓               ↓
┌─────────┐   ┌──────────────────┐
│ 4. ACT  │   │ Respuesta: "No   │
│ ACTIÓN  │   │ entendí"         │
└────┬────┘   └──────────────────┘
     │
     ↓
┌─────────────────────────────────┐
│ 5. RESPUESTA POR VOZ            │
│ - Confirmación de acción        │
│ - Mensaje de resultado          │
└─────────────────────────────────┘
```

### Ejemplo de Procesamiento Detallado

**Entrada:** "Centauro, reproduce soda stereo"

1. **Captura STT**: Audio convertido a texto → "centauro reproduce soda stereo"
2. **Normalización**: "centauro reproduce soda stereo" → ["centauro", "reproduce", "soda", "stereo"]
3. **Validación**: ✓ Palabra de activación reconocida, ✓ Verbo válido, ✓ Complemento válido
4. **Extracción**: verbo="reproduce", objeto="soda stereo"
5. **Acción**: Función `reproducir("soda stereo")` abre YouTube
6. **Respuesta**: Síntesis de voz "Reproduciendo soda stereo"

---

## Métodos de Instalación

### Paso 1: Clonar o Descargar

```CMD
git clone https://github.com/Davbichobeto/mi-asistente-de-voz.git
cd mi-asistente-de-voz
```

O descargar el archivo ZIP desde GitHub.

### Paso 2: Crear Entorno Virtual

```CMD
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Verificar que el prompt muestre `(.venv)`.

### Paso 3: Actualizar pip

```CMD
python -m pip install --upgrade pip
```

### Paso 4: Instalar Dependencias

```CMD
pip install -r requirements.txt
```

Si PyAudio falla (caso común en Windows):

```CMD
pip install pipwin
pipwin install pyaudio
```

### Paso 5: Instalar SAPI (Opcional pero Recomendado)

Para mejor calidad de síntesis de voz en Windows:

```CMD
pip install pywin32
```

### Paso 6: Ejecutar la Aplicación

```CMD
python Asistente_Voz_IA.py
```

---

## Modos de Ejecución

### Modo Estándar (con Micrófono)

```CMD
python Asistente_Voz_IA.py
```

Requisitos: Micrófono conectado, conexión a Internet.

### Modo Texto (sin Micrófono)

```CMD
$env:ASISTENTE_TEXTO = "1"
python Asistente_Voz_IA.py
```

Entrada: Por teclado en consola.

### Modo Debug

```CMD
$env:ASISTENTE_DEBUG_STT = "1"
$env:ASISTENTE_REPETIR_STT_VOZ = "1"
python Asistente_Voz_IA.py
```

Salida: Información detallada de cada etapa del procesamiento.

---

## Configuración y Personalización

### Archivo de Configuración Principal: config.py

Ubicación: `asistente_voz/config.py`

Contenidos configurables:

```python
# Palabras de activación reconocidas
WAKE_WORDS = ["Centauro"]

# Verbos y acciones asociadas
VERBOS = {
    "reproduce": "youtube",
    "busca": "google",
    "abre": "app"
}

# Rutas de aplicaciones Windows
APP_PATHS = {
    "notepad": "notepad.exe",
    "edge": "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe\\excel\\word\\power point",
    # ... más aplicaciones
}

# Idioma de reconocimiento
LANGUAGE_STT = "es-MX"

# Velocidad y volumen de síntesis
TTS_RATE = 150  # palabras por minuto
TTS_VOLUME = 0.8  # 0.0 a 1.0

# Índice del micrófono
MIC_INDEX = 0
```

### Variables de Entorno

Alternativa a editar `config.py`, estas variables permiten configuración temporal:

| Variable | Efecto | Ejemplo |
|----------|--------|---------|
| `ASISTENTE_TEXTO` | Activar modo consola | `$env:ASISTENTE_TEXTO = "1"` |
| `ASISTENTE_MIC_INDEX` | Seleccionar micrófono | `$env:ASISTENTE_MIC_INDEX = "2"` |
| `ASISTENTE_LANG_STT` | Cambiar idioma | `$env:ASISTENTE_LANG_STT = "es-ES"` |
| `ASISTENTE_TTS_RATE` | Velocidad de voz | `$env:ASISTENTE_TTS_RATE = "200"` |
| `ASISTENTE_TTS_VOLUME` | Volumen de voz | `$env:ASISTENTE_TTS_VOLUME = "0.9"` |
| `ASISTENTE_DEBUG_STT` | Activar debug | `$env:ASISTENTE_DEBUG_STT = "1"` |

---

## Extensión del Sistema

### Agregar un Nuevo Verbo

La extensión requiere cuatro modificaciones coordinadas:

**Modificación 1: config.py**

```python
VERBOS = {
    "reproduce": "youtube",
    "busca": "google",
    "abre": "app",
    "descarga": "download"  # NUEVO VERBO
}
```

**Modificación 2: gramatica.py**

```
VP -> "reproduce" Objeto
    | "busca" Objeto
    | "abre" App
    | "descarga" Objeto
```

**Modificación 3: acciones.py**

```python
def descargar(query):
    """Descarga un archivo especificado."""
    print(f"Descargando: {query}")
    # Implementación específica
```

**Modificación 4: agente.py (en procesar_comando)**

```python
elif verbo == "descarga":
    acciones.descargar(objeto)
    hablar(f"Descargando {objeto}")
```

### Cambiar Idioma del Reconocimiento

En `config.py`:

```python
LANGUAGE_STT = "es-ES"   # Español de España
LANGUAGE_STT = "en-US"   # Inglés estadounidense
LANGUAGE_STT = "fr-FR"   # Francés
```

O mediante variable de entorno:

```CMD
$env:ASISTENTE_LANG_STT = "es-ES"
```

---

## Ejemplos de Comandos

La estructura de los comandos sigue el patrón: `[palabra_activación] [verbo] [complemento]`

### Reproducción de Contenido

```
centauro reproduce soda stereo
cortana reproduce musica clasica
google reproduce tutorial python
```

### Búsqueda de Información

```
centauro busca tutorial python
centauro busca recetas veganas
cortana busca noticias tecnologia
```

### Apertura de Aplicaciones

```
centauro abre el notepad
centauro abre edge
centauro abre word
```

---

## Base de Conocimientos: Sistema Experto de Animales

El módulo `Base_Hechos.py` implementa un sistema experto independiente para identificación de animales mediante características.

### Estructura de Datos

```python
BASE_DE_CONOCIMIENTOS = {
    "León": ["melena", "rugido", "salvaje", "carnívoro", "felino"],
    "Gato": ["rasca", "juega", "maulla", "independiente", "pelaje"],
    "Perro": ["ladra", "juega", "pelaje", "domesticado", "obedece"],
    # ... 60+ especies
}
```

### Integración Potencial

Extensión futura para comandos como "describe el león":

```python
elif verbo == "describe":
    animal = objeto.capitalize()
    if animal in BASE_DE_CONOCIMIENTOS:
        rasgos = ", ".join(BASE_DE_CONOCIMIENTOS[animal])
        hablar(f"El {animal} tiene: {rasgos}")
```

---

## Solución de Problemas

| Problema | Causa | Solución |
|----------|-------|----------|
| PyAudio no se instala | Faltan compiladores o wheels precompiladas | Usar `pipwin install pyaudio` |
| El asistente no escucha | Micrófono no configurado o permiso denegado | Ejecutar con `ASISTENTE_LISTAR_MICS=1` para identificar dispositivo |
| Sin respuesta de voz | SAPI no disponible | Instalar `pywin32` o forzar `ASISTENTE_TTS_PYTTSX3=1` |
| "No entendí" frecuente | Ruido de fondo alto | Aumentar `ASISTENTE_ESCUCHA_TIMEOUT`, revisar calibración |
| Gramática rechaza frases | Formato incorrecto | Verificar orden: palabra_activación + verbo + complemento |
| Bajo reconocimiento | Idioma incorrecto o micrófono deficiente | Cambiar `ASISTENTE_LANG_STT` o verificar calidad de audio |

---

## Arquitectura de Datos

### Flujo de Información

```
Audio (micrófono)
        ↓
[voz_stt.py] → Google Cloud Speech API
        ↓
Texto normalizado
        ↓
[texto.py] → Minúsculas, sin acentos, tokens
        ↓
[gramatica.py] → Validación CFG → Extracción verbo/objeto
        ↓
[agente.py] → Despacho a acción específica
        ↓
[acciones.py] → Ejecución (YouTube, Google, subprocess)
        ↓
[voz_tts.py] → Síntesis de voz
        ↓
Respuesta audible (altavoz)
```

### Estructura de Directorios

```
Asistente_Centauro/
├── asistente_voz/
│   ├── __init__.py
│   ├── agente.py                # Orquestador
│   ├── config.py                # Configuración
│   ├── gramatica.py             # Validador
│   ├── texto.py                 # Normalizador
│   ├── voz_stt.py               # Entrada de audio
│   ├── voz_tts.py               # Salida de audio
│   ├── acciones.py              # Ejecutor de tareas
│   ├── arrancar.py              # Utilidad
│   ├── prueba_mic.py            # Diagnóstico
│   └── test_mic.py              # Diagnóstico
├── Asistente_Voz_IA.py          # Punto de entrada
├── Base_Hechos.py               # Sistema experto
├── requirements.txt             # Dependencias
├── README.md                     # Documentación
└── .git/                         # Control de versiones
```

---

## Características de Calidad

### Manejo de Errores

El sistema implementa captura de excepciones en:
- Caída de conexión a Google Cloud
- Dispositivos de audio no disponibles
- Frases malformadas
- Comandos no reconocidos

### Validación de Entrada

- Gramática formal previene ejecución de comandos inválidos
- Normalización de texto mitiga errores de reconocimiento menores
- Confirmación de acciones por voz antes de ejecución

### Extensibilidad Demostrada

El código está diseñado para agregar:
- Nuevos verbos sin modificar el núcleo
- Nuevas aplicaciones en Windows sin cambiar la lógica
- Nuevas integraciones con servicios web
- Soporte para múltiples idiomas

---

## Casos de Uso Demostrados

1. **Entretenimiento**: Reproducción de música y videos mediante comando de voz
2. **Productividad**: Apertura rápida de aplicaciones de oficina
3. **Búsqueda de Información**: Consultas directas a Google desde la voz
4. **Educación**: Aprendizaje de conceptos de NLP, reconocimiento de voz, gramáticas formales
5. **Accesibilidad**: Control mediante voz para usuarios con limitaciones motoras

---

## Cálculo de Instalación

**Tiempo total estimado: 8-12 minutos**

- Descargar/clonar: 1 minuto
- Crear entorno virtual: 1 minuto
- Instalar dependencias: 5-8 minutos (PyAudio puede ser lento)
- Configuración básica: 2 minutos
- Primera ejecución: 1 minuto

**Espacio requerido:**

- Código fuente: ~150 KB
- Entorno virtual (.venv): ~200-300 MB
- Dependencias instaladas: ~100-150 MB
- **Total: ~500 MB**

---

## Verificación de Instalación

```CMD
# Verificar entorno activado
echo $env:VIRTUAL_ENV

# Verificar versión de Python
python --version

# Verificar instalación de dependencias
pip list

# Verificar acceso a micrófono (opcional)
$env:ASISTENTE_LISTAR_MICS = "1"
python Asistente_Voz_IA.py

# Ejecutar en modo texto para prueba sin micrófono
$env:ASISTENTE_TEXTO = "1"
python Asistente_Voz_IA.py
```

---

## Resumen Ejecutivo

**Asistente Centauro** es un sistema completo de procesamiento de comandos de voz que combina:
- Reconocimiento automático de voz mediante Google Cloud
- Validación rigurosa mediante gramáticas formales
- Ejecución flexible de acciones predefinidas
- Síntesis de voz para realimentación del usuario

Su arquitectura modular, documentación exhaustiva y configuración centralizada lo convierten en una base sólida tanto para uso inmediato como para extensión y experimentación en procesamiento de lenguaje natural.

**Características clave:**
✓ Totalmente en español  
✓ Modular y extensible  
✓ Múltiples modos de operación  
✓ Documentación completa  
✓ Sistema experto integrado  
✓ Validación gramical rigurosa  
✓ Soporte multiidioma  

---

## Próximos Pasos

1. Seguir los pasos de instalación en orden
2. Ejecutar en modo texto para familiarizarse sin micrófono
3. Consultar `config.py` para personalización
4. Experimentar con nuevos comandos
5. Extender con nuevas acciones según necesidades específicas

