import json
import glob

def merge_json_files(directory, output_file):
    """
    Объединяет данные из нескольких JSON файлов в один.

    :param directory: Путь к директории с JSON файлами.
    :param output_file: Путь к выходному JSON файлу.
    """
    # Поиск всех JSON файлов в указанной директории
    json_files = glob.glob(f"{directory}/*.json")

    # Общий список для хранения данных из всех файлов
    all_employees = []

    # Чтение данных из каждого JSON файла и добавление их в общий список
    for file in json_files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            all_employees.extend(data)

    # Сохранение объединенных данных в новый JSON файл
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_employees, f, ensure_ascii=False, indent=4)

# Пример использования функции
merge_json_files(
    directory='path/to/your/directory',
    output_file='path/to/your/all_employees.json'
)
