from pathlib import Path

def save_text_to_file(content: str, filename: str) -> None:

    if not isinstance(content, str):
        raise TypeError("content must be a string")

    if not isinstance(filename, str):
        raise TypeError("filename must be a string")

    if not filename.endswith(".txt"):
        filename += ".txt"

    path = Path(filename)

    path.write_text(content, encoding="utf-8")