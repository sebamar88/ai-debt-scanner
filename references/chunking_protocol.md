# Protocolo de Análisis por Chunks (Fragmentado)

Cuando un archivo es detectado con `[CHUNK REQ]` (Estimación > 1000 tokens), el agente DEBE seguir este protocolo de análisis para evitar saturar el contexto y mantener la coherencia del análisis.

## Parámetros de Segmentación
*   **Tamaño de Chunk**: ~1000 tokens (Aproximadamente 4000 caracteres o 150-200 líneas de código).
*   **Solapamiento (Overlap)**: ~100 tokens (Aproximadamente 400 caracteres o 20 líneas).
*   **Validación de Límites**: Cada interacción con el LLM no debe exceder los límites del modelo (e.g., Gemini 2.0 Flash ~1M, pero para análisis profundo se recomiendan contextos de <10k para mayor precisión en refactorización).

## Flujo de Trabajo

### 1. Lectura Inicial de Estructura
Antes de procesar los chunks, obtén la estructura global del archivo (importaciones, nombres de clases/funciones principales) para tener el mapa mental del archivo.

### 2. Procesamiento de Chunks Iterativo
Para cada archivo de gran tamaño, utiliza `read_file` con `offset` y `limit` de forma secuencial:

*   **Chunk 1**: `offset: 0`, `limit: 200`
*   **Chunk 2**: `offset: 180` (20 líneas de solapamiento), `limit: 200`
*   **Chunk 3**: `offset: 360`, `limit: 200`
*   ... hasta el final del archivo.

### 3. Síntesis de Hallazgos
*   Identifica violaciones que cruzan las fronteras de los chunks (e.g., una función que empieza en el Chunk 1 y termina en el 3).
*   Mantén un registro de las variables globales o estados compartidos entre fragmentos.

### 4. Resolución Quirúrgica
Al proponer cambios, enfócate en el chunk específico. Si el cambio requiere modificar múltiples partes distantes del archivo, realiza los cambios en pasos secuenciales validados individualmente.
