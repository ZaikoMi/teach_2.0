import pygame
import os


def play_chinese_text(text):
    f_name = os.path.join(os.path.dirname(__file__),"audio",''.join([text,'.mp3']))
    pygame.mixer.music.load(f_name)
    pygame.mixer.music.play()
    # Ждём окончания проигрывания
    # while pygame.mixer.music.get_busy():
    #     pygame.time.Clock().tick(10)

