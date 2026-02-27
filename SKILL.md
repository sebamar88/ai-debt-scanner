---
name: ai-debt-scanner
description: Escanea y puntúa la deuda técnica generada por IA ("vibe coding") en proyectos multi-lenguaje. Utiliza heurísticas de análisis estructural (bloat, pereza de IA, redundancia) inspiradas en 'drift' para detectar patrones comunes en código generado por modelos de lenguaje. Úsalo para auditar la calidad del código, identificar archivos monolíticos y encontrar rastros de depuración u olvidos de la IA.
---

# AI Debt Scanner (Multi-Agent Protocol)

## Sistema de Agentes Especializados
Para maximizar la eficiencia, este skill divide las tareas en agentes paralelos que se comunican vía **TOON/JSON**.

### 1. Scanner Agent (The Auditor)
*   **Misión**: Ejecutar `scripts/scan.py --toon` para identificar hotspots.
*   **Input**: Directorio raíz del proyecto.
*   **Output**: Un mapa TOON de "puntos calientes" con índices de tokens.

### 2. Architect Agent (The Mapper)
*   **Misión**: Gestionar archivos `[CHUNK REQ]`. Divide los archivos grandes según `references/chunking_protocol.md`.
*   **Paralelismo**: Puede mapear múltiples archivos grandes simultáneamente.
*   **Output**: Plan de segmentación para el Refactor Agent.

### 3. Cleaner Agent (The Surgeon)
*   **Misión**: Aplicar refactorizaciones quirúrgicas basadas en `references/refactoring_patterns.md`.
*   **Estrategia**: No re-escanea. Confía en los índices `t_idx` provistos por el Scanner Agent.
*   **Validación**: Ejecuta un mini-escaneo post-cambio para asegurar que el `score` bajó.

## Flujo de Trabajo Paralelo
1.  **Scanner** genera el reporte global.
2.  Si hay múltiples archivos con deuda, se instancian **N Cleaners** (uno por archivo o sub-módulo).
3.  Si un archivo es gigante, el **Architect** guía al **Cleaner** a través de chunks.

## Protocolo TOON (Token-Oriented Object Notation)
Este skill utiliza TOON para evitar que la IA lea archivos enteros innecesariamente. 
- `t_idx`: Índice aproximado del token problemático.
- `hotspots`: Lista de coordenadas críticas para intervención inmediata.

