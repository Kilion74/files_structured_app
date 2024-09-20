import os
import shutil
import tkinter as tk
from tkinter import messagebox


def sort_files():
    source_folder = entry.get()  # Получаем путь из текстового поля

    # Проверяем, существует ли заданная папка
    if not os.path.isdir(source_folder):
        messagebox.showerror("Ошибка", "Указанный путь не существует.")
        return

    destination_folder = source_folder

    # Создаем папки для каждой категории, если их еще нет
    folders = ['excel', 'word', 'txt', 'csv']
    for folder in folders:
        os.makedirs(os.path.join(destination_folder, folder), exist_ok=True)

    # Перемещаем файлы в соответствующие папки
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Проверяем, является ли это файлом
        if os.path.isfile(file_path):
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

    messagebox.showinfo("Успех", "Файлы успешно отсортированы.")


# Создаем главное окно
root = tk.Tk()
root.title("Сортировка файлов")

# Создаем метку и текстовое поле для ввода пути
label = tk.Label(root, text="Введите путь к папке:", font=2)
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Создаем кнопку для сортировки файлов
sort_button = tk.Button(root, text="Сортировать файлы", command=sort_files, font=2)
sort_button.pack(pady=10)

# Запускаем главный цикл
root.mainloop()
