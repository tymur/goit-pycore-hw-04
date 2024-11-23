from pathlib import Path

# Створення об'єкту Path для файлу
file_path = Path("example.txt")

# Запис тексту у файл
file_path.write_text("Привіт світ!", encoding="utf-8")

