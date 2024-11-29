import os
import json
import csv
import pickle

def get_directory_size(directory):
    """
    Рекурсивно вычисляет размер директории, включая все вложенные файлы и директории.

    :param directory: Путь к директории.
    :return: Размер директории в байтах.
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def collect_directory_info(directory):
    """
    Рекурсивно обходит директорию и собирает информацию о файлах и директориях.

    :param directory: Путь к директории.
    :return: Список словарей с информацией о файлах и директориях.
    """
    info_list = []

    for root, dirs, files in os.walk(directory):
        for name in dirs + files:
            path = os.path.join(root, name)
            parent = os.path.basename(root)
            item_type = 'directory' if os.path.isdir(path) else 'file'
            size = get_directory_size(path) if item_type == 'directory' else os.path.getsize(path)

            info = {
                'name': name,
                'path': path,
                'type': item_type,
                'size': size,
                'parent': parent
            }
            info_list.append(info)

    return info_list

def save_to_json(data, file_path):
    """
    Сохраняет данные в файл формата JSON.

    :param data: Данные для сохранения.
    :param file_path: Путь к файлу.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_to_csv(data, file_path):
    """
    Сохраняет данные в файл формата CSV.

    :param data: Данные для сохранения.
    :param file_path: Путь к файлу.
    """
    keys = data[0].keys()
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def save_to_pickle(data, file_path):
    """
    Сохраняет данные в файл формата Pickle.

    :param data: Данные для сохранения.
    :param file_path: Путь к файлу.
    """
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

def main(directory):
    """
    Основная функция для сбора информации о директории и сохранения её в разные форматы.

    :param directory: Путь к директории.
    """
    if not os.path.isdir(directory):
        raise ValueError(f"Директория {directory} не существует.")

    info_list = collect_directory_info(directory)

    save_to_json(info_list, 'directory_info.json')
    save_to_csv(info_list, 'directory_info.csv')
    save_to_pickle(info_list, 'directory_info.pkl')

# Пример использования функции
main(directory='path/to/your/directory')
