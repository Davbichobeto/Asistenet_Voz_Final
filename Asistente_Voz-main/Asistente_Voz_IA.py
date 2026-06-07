"""
PUNTO DE ENTRADA PRINCIPAL - Asistente de Voz Centauro
"""

from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from asistente_voz.agente import main
    print("✅ Asistente Centauro cargado correctamente.")
except ImportError as e:
    print(f"❌ Error al importar el agente: {e}")
    print("Verifica que todos los archivos estén en la carpeta 'asistente_voz/'")
    sys.exit(1)


if __name__ == "__main__":
    main()