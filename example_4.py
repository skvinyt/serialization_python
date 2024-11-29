import csv

def calculate_total_revenue(input_csv, output_csv):
    """
    Считывает данные из CSV файла, подсчитывает общую выручку для каждого продукта
    и сохраняет результаты в новый CSV файл.

    :param input_csv: Путь к исходному CSV файлу.
    :param output_csv: Путь к выходному CSV файлу.
    """
    # Словарь для хранения выручки по каждому продукту
    revenue_dict = {}

    # Чтение данных из исходного CSV файла
    with open(input_csv, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row['название продукта']
            quantity = int(row['количество'])
            price = float(row['цена за единицу'])

            # Подсчет выручки для каждого продукта
            if product in revenue_dict:
                revenue_dict[product] += quantity * price
            else:
                revenue_dict[product] = quantity * price

    # Запись данных в новый CSV файл
    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['название продукта', 'общая выручка']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # Запись заголовков
        writer.writeheader()

        # Запись итоговых данных
        for product, revenue in revenue_dict.items():
            writer.writerow({'название продукта': product, 'общая выручка': revenue})

# Пример использования функции
calculate_total_revenue(
    input_csv='path/to/your/sales.csv',
    output_csv='path/to/your/total_sales.csv'
)
