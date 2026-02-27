# AI Refactoring Patterns

Este documento sirve como guía para transformar código con "vibe coding debt" en código idiomático y mantenible.

## 1. Large Functions -> Decomposition
**Problema**: La IA tiende a escribir funciones de >50 líneas que manejan múltiples responsabilidades.

❌ **Bad (IA-style)**:
```python
def process_data(data):
    # logic for validation (20 lines)
    # logic for transformation (30 lines)
    # logic for db saving (10 lines)
    pass
```

✅ **Good**:
```python
def process_data(data):
    validate_data(data)
    transformed = transform_data(data)
    save_to_db(transformed)
```

## 2. Empty Catches -> Resilient Error Handling
**Problema**: Bloques `catch` vacíos o excepciones genéricas.

❌ **Bad (IA-style)**:
```typescript
try {
  doSomething();
} catch (e) {
  // ignore
}
```

✅ **Good**:
```typescript
try {
  doSomething();
} catch (error) {
  if (error instanceof ValidationError) {
    logger.warn("Validation failed", { error });
    return;
  }
  throw error; // Propagate unexpected errors
}
```

## 3. Structural Bloat -> Module Extraction
**Problema**: Archivos de >300 líneas.
**Solución**: Identificar sub-dominios (e.g., helpers, types, api-calls) y moverlos a archivos dedicados.
