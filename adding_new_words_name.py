# main.py
import tkinter as tk
from main import *

from b_conf import *



def creating_file_frame():
    # === 4. Окно: ввод названия файла ===
    create_file_frame = tk.Frame(root, bg="#f0f0f0")
    create_file_frame.grid(row=0, column=0, sticky="nsew")

    # Заголовок
    tk.Label(
        create_file_frame,
        text="Adding words / Добавление слов",
        font=("Arial", 24),
        bg="#f0f0f0"
    ).pack(pady=40)


    tk.Label(
        create_file_frame,
        text="File name / Имя файла:",
        font=("Arial", 16),
        bg="#f0f0f0"
    ).pack(pady=10)

    # Поле ввода
    file_name_entry = tk.Entry(
        create_file_frame,
        font=("Arial", 18),
        width=30,
        justify="center"
    )
    file_name_entry.pack(pady=10, ipady=5)

    # Кнопки
    button_frame = tk.Frame(create_file_frame, bg="#f0f0f0")
    button_frame.pack(pady=(400,30))

    def on_ok_click():
        global new_file_name
        name = file_name_entry.get().strip()
        if not name:
            print("Имя файла не может быть пустым")
            return
        new_file_name = name
        file_name_entry.delete(0, tk.END)  # очистить поле

    # Кнопка ОК
    tk.Button(
        button_frame,
        text="OK / Готово",
        **button_config_x,
        command=on_ok_click
    ).pack(padx=15,pady=(0,25))

    # Кнопка Назад
    tk.Button(
        button_frame,
        text="Back / Назад",
        **back_button_config,
        command=lambda: show_frame(main_frame)
    ).pack(padx=15)
    return create_file_frame

print(type(creating_file_frame()))


