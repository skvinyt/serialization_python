import csv
import json

def csv_to_json_by_author(input_csv, output_json):
    """
    Считывает данные из CSV файла и сохраняет их в JSON файл, где книги
    сгруппированы по авторам.

    :param input_csv: Путь к исходному CSV файлу.
    :param output_json: Путь к выходному JSON файлу.
    """
    # Словарь для хранения книг по авторам
    books_by_author = {}

    # Чтение данных из CSV файла
    with open(input_csv, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            author = row['автор']
            book = {
                'название': row['название'],
                'год издания': row['год издания']
            }

            # Группировка книг по авторам
            if author in books_by_author:
                books_by_author[author].append(book)
            else:
                books_by_author[author] = [book]

    # Запись данных в JSON файл
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(books_by_author, f, ensure_ascii=False, indent=4)

# Пример использования функции
csv_to_json_by_author(
    input_csv='path/to/your/books.csv',
    output_json='path/to/your/books_by_author.json'
)
