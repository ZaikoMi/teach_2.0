# main.py
import tkinter as tk
from b_conf import *
from logic_for_traning import *

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
training_frame = tk.Frame(root, bg="#f0f0f0")
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
    command=lambda: show_frame(add_frame)
).pack(pady=30, padx=100, fill=tk.X)


# === 2. Страница "Training" ===
tk.Label(training_choose_frame, text="Select a training type", font=("Arial", 24), bg="#f0f0f0").pack(pady=20)
tk.Label(training_choose_frame, text="选择训练类型", font=("Arial", 18), bg="#f0f0f0").pack(pady=10)
my_list_of_files = Training()

for file in my_list_of_files:
    tk.Button(
        training_choose_frame,
        text=file,
        **button_config_x,
        command= lambda f=file: print(f'open {f}')
    ).pack(pady=10, padx=80, fill=tk.X)


# Кнопка "Назад"
tk.Button(
    training_choose_frame,
    text="Back / 返回",
    **back_button_config,
    command=lambda: show_frame(main_frame)
).pack(pady=40)


# === 3. Страница "Add" ===
tk.Label(add_frame, text="Add new exercise or word", font=("Arial", 24), bg="#f0f0f0").pack(pady=20)
tk.Label(add_frame, text="添加新的练习或单词", font=("Arial", 18), bg="#f0f0f0").pack(pady=10)

tk.Button(
    add_frame,
    text="Add Word / 添加单词",
    **button_config,
    command=lambda: print("Adding new word...")
).pack(pady=20, padx=80, fill=tk.X)

tk.Button(
    add_frame,
    text="Add Sentence / 添加句子",
    **button_config2,
    command=lambda: print("Adding new sentence...")
).pack(pady=20, padx=80, fill=tk.X)

tk.Button(
    add_frame,
    text="Back / 返回",
    **back_button_config,
    command=lambda: show_frame(main_frame)
).pack(pady=40)


# === Запуск: показываем сначала главную страницу ===
show_frame(main_frame)

# Запуск приложения
root.mainloop()