import tkinter as tk
from tkinter import font as tkfont


def create_responsive_label(parent, text):
    current_font = tkfont.Font(family="Arial", size=60)

    label = tk.Label(
        parent,
        text=text,
        font=current_font,
        bg="#f0f0f0",
        fg="black",
        wraplength=800,
        justify="center"
    )
    label.pack(pady=(20, 50), fill="both", expand=True)

    def on_resize(event):
        if event.width <= 50 or event.height <= 50:  # защита от мусора
            return
        label.config(wraplength=event.width - 40)
        new_size = int(min(event.width, event.height) / 15)
        new_size = max(12, min(new_size, 120))
        current_font.config(size=new_size)

    parent.bind("<Configure>", on_resize)

    return label