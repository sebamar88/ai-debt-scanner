# AI Debt Scanner Skill 🚀

Un skill diseñado para auditar y limpiar la deuda técnica generada por IA (el llamado "vibe coding") en proyectos multi-lenguaje. Utiliza heurísticas de análisis estructural para detectar patrones comunes en código generado por modelos de lenguaje, como bloques de código muerto, funciones gigantescas, comentarios de la propia IA y manejo pobre de excepciones.

## Características

- 🔍 **Agnóstico al Lenguaje:** Soporta Python, TypeScript, JavaScript, Go, Rust, Java, y C++.
- ⚖️ **Puntuación de Deuda (Debt Scoring):** Evalúa cada archivo y el proyecto en general con un sistema de pesos.
- 🤖 **Detección de Artefactos de IA:** Encuentra rastros de conversaciones de IA, excusas u olvidos ("as an AI model...", "I can help with...").
- 📦 **Soporte TOON (Token-Oriented Object Notation):** Salida optimizada para reducir el consumo de tokens en LLMs en un 40%.
- 🤝 **Arquitectura Multi-Agente:** Sistema modular con agentes especializados (Scanner, Architect, Cleaner).

## Estructura del Proyecto

```
.
├── SKILL.md                 # Definición del skill y protocolo multi-agente
├── agents/                  # Agentes especializados (Scanner, Architect, Cleaner)
├── scripts/
│   └── scan.py              # Script principal con salida TOON/JSON
├── references/              # Reglas y patrones de refactorización
└── tests/                   # Muestras de código con deuda para validación
```

## Uso

Para escanear un directorio, ejecuta el script de escaneo con Python:

```bash
python3 scripts/scan.py /ruta/a/tu/proyecto
```

Si no especificas una ruta, escaneará el directorio actual por defecto:

```bash
python3 scripts/scan.py .
```

### Ejemplo de Salida

```text
========================================
AI DEBT SCAN REPORT
========================================
Project Temperature: 35.50/100
Overall Grade: Moderate ⚠️
Scanned Files with Debt: 2
----------------------------------------
[ 30] src/utils.py (~450 tokens)
      - L45: AI Artifact (AI meta-talk found in source code)
[ 15] src/main.ts (~1200 tokens) [CHUNK REQ]
      - L12: Empty Catch (Empty catch/except block)
      - L89: TODO Leftover (Unresolved TODO/FIXME)
```

## Próximos Pasos

Este repositorio está pensado para ser utilizado como un "Skill" por agentes CLI (como Gemini CLI). Una vez que el agente corre el escáner, puede usar el contexto provisto en la carpeta `references/` para arreglar el código de forma automática.
