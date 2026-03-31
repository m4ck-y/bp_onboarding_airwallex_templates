#!/usr/bin/env python3
"""
Script para ordenar alfabeticamente el archivo dev.env.json por el campo 'name'
"""

import json
from pathlib import Path


def sort_env_json(input_file: str, output_file: str = None) -> None:
    """
    Ordena un archivo JSON alfabeticamente por el campo 'name'.
    
    Args:
        input_file: Ruta al archivo JSON de entrada
        output_file: Ruta al archivo JSON de salida (si es None, sobrescribe el original)
    """
    input_path = Path(input_file)
    
    # Leer el archivo JSON
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Verificar que es una lista
    if not isinstance(data, list):
        raise ValueError("El archivo JSON debe ser una lista de objetos")
    
    print(f"📊 Total de items antes de ordenar: {len(data)}")
    
    # Ordenar por el campo 'name'
    sorted_data = sorted(data, key=lambda x: x.get('name', '').lower())
    
    print(f"📊 Total de items despues de ordenar: {len(sorted_data)}")
    
    # Determinar archivo de salida
    if output_file is None:
        output_file = input_file
    
    output_path = Path(output_file)
    
    # Escribir el resultado con indentación de 2 espacios
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(sorted_data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Archivo ordenado: {output_path}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
    else:
        input_path = "dev.env.json"
        output_path = None
    
    sort_env_json(input_path, output_path)