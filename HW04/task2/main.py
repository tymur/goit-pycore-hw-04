import os
def get_cats_info(path):
    """
    Читає файл з інформацією про котів і повертає список словників.

    Параметри:
        path (str): Шлях до текстового файлу.

    Повертає:
        list: Список словників, де кожен словник містить інформацію про кота.
    """
    cats_info = []

    try:
        # Читання файлу з використанням менеджера контексту
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                # Видалення зайвих пробілів і розділення даних
                cat_id, name, age = line.strip().split(",")
                
                # Формування словника для кожного кота
                cat_dict = {"id": cat_id, "name": name, "age": age}
                cats_info.append(cat_dict)

        return cats_info

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return []
    except ValueError:
        print("Помилка у форматі даних. Перевірте вміст файлу.")
        return []

if __name__ == "__main__":
    # Шлях до файлу
    path_to_file = os.path.join(os.path.dirname(__file__), "cats_info.txt")
    
    # Виклик функції
    try:
        cats_info = get_cats_info(path_to_file)
        print(cats_info)
    except Exception as e:
        print(f"Помилка: {e}")
