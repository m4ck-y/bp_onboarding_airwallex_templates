def normalize_to_upper_snake(text: str) -> str:
    text = text.strip()
    text = text.upper()
    partes = text.split()
    return "_".join(partes)