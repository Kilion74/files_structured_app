import os
import shutil

print('Укажите путь к папке...')
case_name = input()
# Укажите путь к папке "Документы"
source_folder = fr'{case_name}'
# Укажите путь к папке, где будете создавать новые папки
destination_folder = source_folder

# Создаем папки для каждой категории, если их еще нет
folders = ['excel', 'word', 'txt', 'csv', 'mp4', 'exe']
for folder in folders:
    os.makedirs(os.path.join(destination_folder, folder), exist_ok=True)

# Перебираем все файлы в папке "Документы"
for filename in os.listdir(source_folder):
    # Полный путь к файлу
    file_path = os.path.join(source_folder, filename)

    # Проверяем, является ли это файлом
    if os.path.isfile(file_path):
        # Определяем расширение файла
        _, ext = os.path.splitext(filename)

        # Перемещаем файл в соответствующую папку
        if ext in ['.xlsx', '.xls']:
            shutil.move(file_path, os.path.join(destination_folder, 'excel', filename))
        elif ext in ['.docx', '.doc']:
            shutil.move(file_path, os.path.join(destination_folder, 'word', filename))
        elif ext in ['.txt']:
            shutil.move(file_path, os.path.join(destination_folder, 'txt', filename))
        elif ext in ['.csv']:
            shutil.move(file_path, os.path.join(destination_folder, 'csv', filename))
        elif ext in ['.mp4']:
            shutil.move(file_path, os.path.join(destination_folder, 'mp4', filename))
        elif ext in ['.exe']:
            shutil.move(file_path, os.path.join(destination_folder, 'exe', filename))

print("Файлы были успешно структурированы по категориям.")