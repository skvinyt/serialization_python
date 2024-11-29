import json
import csv

def json_to_csv(json_file, csv_file):
    """
    Считывает данные из JSON файла и сохраняет их в CSV файл.

    :param json_file: Путь к JSON файлу.
    :param csv_file: Путь к CSV файлу.
    """
    # Чтение данных из JSON файла
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Запись данных в CSV файл
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        # Определение заголовков CSV файла
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # Запись заголовков
        writer.writeheader()

        # Запись данных
        for item in data:
            writer.writerow(item)

# Пример использования функции
json_to_csv(
    json_file='path/to/your/products.json',
    csv_file='path/to/your/products.csv'
)
