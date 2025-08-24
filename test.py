from gtts import gTTS
import pygame
import os
import tempfile

from logic_for_training import training, Voc


def save_tts(filename):
    tts = gTTS(text=filename, lang='en')
    tts.save(''.join(["audio/", filename, ".mp3"]))
    print(f"Аудио сохранено: {filename}")

# l = Voc("z_all_of_my")

# for i in l.list_of_words:
#     w = i.split('/')
#     w =w[1].split(maxsplit=1)[0]
#     # print(w)
#     save_tts(w)
#
save_tts('家')