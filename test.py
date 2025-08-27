#from gtts import gTTS
# import pygame
# import os
# import tempfile
import tkinter as tk
#
# from logic_for_training import training, Voc
#
# #
# # def save_tts(filename):
# #     tts = gTTS(text=filename, lang='en')
# #     tts.save(''.join(["audio/", filename, ".mp3"]))
# #     print(f"Аудио сохранено: {filename}")
#
# # l = Voc("z_all_of_my")
#
# # for i in l.list_of_words:
# #     w = i.split('/')
# #     w =w[1].split(maxsplit=1)[0]
# #     # print(w)
# #     save_tts(w)
# #
# # save_tts('家')
#
# l_L = []
# l = Voc("7. All of my")
# for i in l.list_of_words:
#     l_L.append(i.split('/')[0])
# print(','.join(l_L))

import tkinter as tk
from tkinter import font

root = tk.Tk()
fonts = list(font.families())
chinese_fonts = [f for f in fonts if any(lang in f.lower() for lang in ['hei', 'song', 'kai', 'liu', 'yahei', 'ming'])]
print("Вероятно китайские шрифты:")
for f in sorted(chinese_fonts):
    print(f)


root = tk.Tk()
root.title("My Training 2.0")
root.geometry("1000x800")
root.configure(bg="#f0f0f0")

# Чтобы фреймы растягивались
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# --- Создаём фреймы (страницы) ---
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.grid(row=0, column=0, sticky="nsew")

# === Функции переключения страниц ===
def show_frame(frame):
    frame.tkraise()  # поднимает фрейм наверх (делает видимым)

# === 1. Главная страница ===
tk.Label(main_frame, text="选择菜单项", font=("Microsoft YaHei", 70), bg="#f0f0f0").pack(pady=10)
tk.Label(main_frame, text="选择菜单项", font=("SimHei", 70), bg="#f0f0f0").pack(pady=10)
tk.Label(main_frame, text="选择菜单项", font=("FangSong", 70), bg="#f0f0f0").pack(pady=10)
tk.Label(main_frame, text="选择菜单项", font=("KaiTi", 70), bg="#f0f0f0").pack(pady=10)
tk.Label(main_frame, text="选择菜单项", font=("SimSun", 70), bg="#f0f0f0").pack(pady=10)
tk.Label(main_frame, text="选择菜单项", font=("NSimSun", 70), bg="#f0f0f0").pack(pady=10)
show_frame(main_frame)
root.mainloop()

