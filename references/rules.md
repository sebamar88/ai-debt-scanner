# AI Debt Scanner Rules

Este documento define las reglas de puntuación para detectar "vibe coding" y deuda técnica generada por IA.

## Per-File Scoring Logic
Cada archivo comienza con una puntuación de **0**. Se suman pesos por cada violación detectada. El puntaje máximo por archivo es **100**.

### 1. Structural Bloat (Abultamiento Estructural)
*   **Large File (>300 lines)**: `+20` - Archivos monolíticos que la IA no separa.
*   **Large Function (>50 lines)**: `+15` - Funciones que la IA no refactoriza.
*   **High Complexity (Cyclomatic > 10)**: `+15` - Lógica de control profunda y anidada.

### 2. AI Laziness (Pereza de IA)
*   **Console/Debug Leftovers**: `+5` (por instancia, max 15) - `console.log`, `print`, `debugger` olvidados.
*   **TODO/FIXME Comments**: `+5` (por instancia, max 15) - Tareas pendientes no resueltas.
*   **Empty Catch Blocks**: `+10` - Silenciar errores para que el código "simplemente funcione".
*   **Any Abuse (TS/JS specific)**: `+8` - Uso excesivo de `any` en lugar de interfaces.
*   **Generic Exceptions (Python/others)**: `+8` - `except Exception:` o `catch (Exception e)`.

### 3. Redundancy & Patterns (Redundancia y Patrones)
*   **Magic Numbers**: `+5` - Números literales sin constantes explicativas.
*   **Semantic Duplication**: `+20` - Bloques de código idénticos con diferentes nombres.

## Project Debt Temperature
El puntaje del proyecto es el promedio aritmético de todos los archivos analizados.

*   **0–19 (Low)**: ✅ Safe to ship.
*   **20–44 (Moderate)**: ⚠️ Review recommended.
*   **45–69 (High)**: ❌ Significant debt. AI cleanup required.
*   **70–100 (Critical)**: 💀 High risk. Manual rewrite suggested.
