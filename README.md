# docs_expediente_airwallex

Repositorio para documentación y scripts de expediente Airwallex.

## Scripts

### sort_env_json.py

Ordena alfabéticamente un archivo JSON por el campo `name`.

```bash
# Ejecutar con el archivo por defecto (dev.env.json)
python3 scripts/sort_env_json.py

# Ejecutar con un archivo específico
python3 scripts/sort_env_json.py dev.env.json

# Especificar archivo de salida (opcional)
python3 scripts/sort_env_json.py dev.env.json dev_sorted.json
```

**Salida esperada:**
```
📊 Total de items antes de ordenar: 73
📊 Total de items despues de ordenar: 73
✓ Archivo ordenado: dev.env.json