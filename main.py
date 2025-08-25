# main.py
import tkinter as tk


from b_conf import *
from logic_for_training import *

import pygame

from voice_acting import play_chinese_text
from text_auto_editing import create_responsive_label

my_word_class = None
long = '______________________________'
new_file_name = None
# Инициализация pygame для проигрывания
pygame.mixer.init()

# === Главное окно ===
root = tk.Tk()
root.title("My Training 2.0")
root.geometry("1000x800")
root.configure(bg="#f0f0f0")

# Чтобы фреймы растягивались
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# --- Создаём фреймы (страницы) ---
# Каждый фрейм будет "страницей"
main_frame = tk.Frame(root, bg="#f0f0f0")
training_choose_frame = tk.Frame(root, bg="#f0f0f0")
add_frame = tk.Frame(root, bg="#f0f0f0")


# Размещаем все фреймы на том же месте (0,0), но виден будет только один
for frame in (main_frame, training_choose_frame, add_frame):
    frame.grid(row=0, column=0, sticky="nsew")


# === Функции переключения страниц ===
def show_frame(frame):
    """Показывает указанный фрейм"""
    frame.tkraise()  # поднимает фрейм наверх (делает видимым)


# === 1. Главная страница ===
tk.Label(main_frame, text="Choose from the menu", font=("Arial", 30), bg="#f0f0f0").pack(pady=20)
tk.Label(main_frame, text="选择菜单项", font=("Arial", 25), bg="#f0f0f0").pack(pady=10)

# Кнопки перехода
tk.Button(
    main_frame,
    text="Training / 任务型练习",
    **button_config,
    command=lambda: show_frame(training_choose_frame)
).pack(pady=30, padx=100, fill=tk.X)

tk.Button(
    main_frame,
    text="Add / 添加",
    **button_config2,
    command=lambda: show_frame(create_file_frame)
).pack(pady=30, padx=100, fill=tk.X)


# === 2. Страница "Training" ===
tk.Label(training_choose_frame, text="Select a training type", font=("Arial", 24), bg="#f0f0f0").pack(pady=20)
tk.Label(training_choose_frame, text="选择训练类型", font=("Arial", 18), bg="#f0f0f0").pack(pady=10)
my_list_of_files = training()

my_list_of_files = training()
for file in my_list_of_files:
    tk.Button(
        training_choose_frame,
        text=file,
        **button_config_x,
        command=lambda f=file: making_training_page(f)
    ).pack(pady=10, padx=80, fill=tk.X)

# === 2.1 Страница "Training" ===
def making_training_page(name_of_file, new = True):
    global my_word_class
    if new == True:
        my_word_class = Voc(name_of_file)
    training_frame = tk.Frame(root, bg="#f0f0f0")
    training_frame.grid(row=0, column=0, sticky="nsew")
    try:
        play_chinese_text(my_word_class.answer_hanzi)
    except:
        play_chinese_text("no audio file")
    tk.Label(training_frame, text=my_word_class.answer_hanzi, font=("Arial", 160), bg="#f0f0f0").pack(pady=(30,5))
    tk.Label(training_frame, text=my_word_class.answer_pinin, font=("Arial", 20), bg="#f0f0f0").pack(pady=(5, 10))
    my_word_class.inf_for_training_frame()
    # Горизонтальная линия (разделитель)
    tk.Label(training_frame, text=long * 2, font=("Arial", 30), bg="#f0f0f0").pack(pady=(30, 5))
    create_responsive_label(training_frame,my_word_class.question)



    tk.Button(
        training_frame,
        text="Обновить",
        **button_config_x,
        command=lambda f=file: making_training_page(f, new = False)
    ).pack(pady=(0,5), padx=100, fill=tk.X)
    show_frame(training_frame)

    tk.Button(
        training_frame,
        text="Back",
        **button_config_x,
        command=lambda: show_frame(training_choose_frame)
    ).pack(pady=(0,10), padx=100, fill=tk.X)

    # === Хоткеи ===
    training_frame.focus_set()  # позволяет ловить события клавиш

    # Пробел — обновить слово
    training_frame.bind("<space>", lambda f=file: making_training_page(f, new = False))

    # Escape — назад
    training_frame.bind("<Escape>", lambda event: show_frame(training_choose_frame))

    # Enter — альтернатива пробелу (по желанию)
    training_frame.bind("<Return>", lambda f=file: making_training_page(f, new = False))

    # Сохраняем ссылки на биндинги, чтобы GC не удалил
    training_frame.bindings = ["<space>", "<Escape>", "<Return>"]

# Кнопка "Назад"
tk.Button(
    training_choose_frame,
    text="Back / 返回",
    **back_button_config,
    command=lambda: show_frame(main_frame)
).pack(pady=40)


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
    show_frame(fill_file_frame)



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


# === 4. Окно: ввода слов ===
fill_file_frame = tk.Frame(root, bg="#f0f0f0")
fill_file_frame.grid(row=0, column=0, sticky="nsew")
# === Хоткеи ===
fill_file_frame.focus_set()  # позволяет ловить события клавиш

    # Сохраняем ссылки на биндинги, чтобы GC не удалил
fill_file_frame.bindings = ["<space>", "<Escape>", "<Return>"]
# Заголовок
tk.Label(
    fill_file_frame,
    text="Adding words / Добавление слов",
    font=("Arial", 24),
    bg="#f0f0f0"
).pack(pady=40)


tk.Label(
    fill_file_frame,
    text="Hanzi",
    font=("Arial", 15),
    bg="#f0f0f0"
).pack(pady=10)
# Поле ввода
fill_hanzi = tk.Entry(
    fill_file_frame,
    font=("Arial", 18),
    width=30,
    justify="center"
)
fill_hanzi.pack(pady=10, ipady=5)
tk.Label(
    fill_file_frame,
    text="Pinin",
    font=("Arial", 15),
    bg="#f0f0f0"
).pack(pady=10)
# Поле ввода
fill_pinin = tk.Entry(
    fill_file_frame,
    font=("Arial", 18),
    width=30,
    justify="center"
)
fill_pinin.pack(pady=10, ipady=5)

tk.Label(
    fill_file_frame,
    text="Translate",
    font=("Arial", 15),
    bg="#f0f0f0"
).pack(pady=10)
# Поле ввода
fill_translation = tk.Entry(
    fill_file_frame,
    font=("Arial", 18),
    width=30,
    justify="center"
)
fill_translation.pack(pady=10, ipady=5)


def on_ok_click():
    hanzi_name = fill_hanzi.get().strip()
    pinin_name = fill_pinin.get().strip()
    translstion_name = fill_translation.get().strip()
    if not hanzi_name or not pinin_name or not translstion_name:
        print("Поле не может быть пустым")
        return


    with open(os.path.join(get_path(), 'words', new_file_name), "a", encoding="utf-8") as file:
        file.write(''.join([hanzi_name,'/', pinin_name," ", translstion_name]) + "\n")
    print(''.join([hanzi_name,'/', pinin_name," ", translstion_name]))
    fill_hanzi.delete(0, tk.END)  # очистить поле
    fill_pinin.delete(0, tk.END)  # очистить поле
    fill_translation.delete(0, tk.END)  # очистить поле


# Кнопки
button_frame = tk.Frame(fill_file_frame, bg="#f0f0f0")
button_frame.pack(pady=(200,30))

# Кнопка ОК
tk.Button(
    button_frame,
    text="OK / Готово",
    **button_config_x,
    command=on_ok_click
).pack(padx=15,pady=(10,25))

# Кнопка Назад
tk.Button(
    button_frame,
    text="Back / Назад",
    **back_button_config,
    command=lambda: show_frame(main_frame)
).pack(padx=15)

show_frame(fill_file_frame)
# root.mainloop()






# === Запуск: показываем сначала главную страницу ===
show_frame(main_frame)

# Запуск приложения
root.mainloop()