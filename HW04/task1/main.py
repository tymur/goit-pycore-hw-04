import os
def total_salary(path):
    """
    Розраховує загальну та середню заробітну плату розробників з текстового файлу.

    Параметри:
        path (str): Шлях до текстового файлу.

    Повертає:
        tuple: Кортеж із загальної та середньої заробітної плати.
    """
    try:
        total = 0
        count = 0

        # Відкриваємо файл з використанням менеджера контексту with
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                # Розділяємо рядок на ім'я та зарплату
                _, salary = line.strip().split(",")
                total += int(salary)  # Додаємо зарплату до загальної суми
                count += 1  # Збільшуємо кількість розробників

        if count == 0:
            return (0, 0)  # Якщо файл порожній, повертаємо нулі

        # Розраховуємо середню зарплату
        average = total / count
        return (total, average)

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return (0, 0)
    except ValueError:
        print("Помилка у форматі даних. Перевірте вміст файлу.")
        return (0, 0)


if __name__ == "__main__":
    # Вкажіть шлях до файлу з даними
    path_to_file = os.path.join(os.path.dirname(__file__), "salaries.txt")
    
    # Виклик функції
    total, average = total_salary(path_to_file)
    print(f"Загальна сума заробітної плати: {round(total, 2):.2f}")
    print(f"Середня заробітна плата: {round(average, 2):.2f}")
