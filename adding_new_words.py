from main import *
from b_conf import *
from adding_new_words_name import new_file_name


# === 4. Окно: ввод названия файла ===
fill_file_frame = tk.Frame(root, bg="#f0f0f0")
fill_file_frame.grid(row=0, column=0, sticky="nsew")

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

# Кнопки
button_frame = tk.Frame(fill_file_frame, bg="#f0f0f0")
button_frame.pack(pady=(10,30))

def on_ok_click():
    hanzi_name = fill_hanzi.get().strip()
    pinin_name = fill_pinin.get().strip()
    translstion_name = fill_translation.get().strip()
    if not hanzi_name or not pinin_name or not translstion_name:
        print("Имя файла не может быть пустым")
        return
    print(' '.join([hanzi_name, pinin_name, translstion_name]))
    fill_hanzi.delete(0, tk.END)  # очистить поле
    fill_pinin.delete(0, tk.END)  # очистить поле
    fill_translation.delete(0, tk.END)  # очистить поле

# Кнопка ОК
tk.Button(
    button_frame,
    text="OK / Готово",
    **button_config_x,
    command=on_ok_click
).pack(padx=15,pady=(180,25))

# Кнопка Назад
tk.Button(
    button_frame,
    text="Back / Назад",
    **back_button_config,
    command=lambda: show_frame(main_frame)
).pack(padx=15)

show_frame(fill_file_frame)
# root.mainloop()


