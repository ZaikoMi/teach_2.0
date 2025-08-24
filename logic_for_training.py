from collections.abc import list_iterator
from random import choice, random
import os, os.path



def get_path():
    return os.path.dirname(__file__)

def training():
    current_dir = get_path()
    path =  os.path.join(current_dir, 'words')
    all_files = os.listdir(path)
    list_of_files = []
    for f_name in all_files:
        list_of_files.append(f_name)
    return list_of_files

class Voc:
    def __init__(self, name):
        self.path = os.path.join(get_path(), 'words', name)
        self.list_of_words = self.make_list_of_words()
        self.question = " "
        self.answer = " "


    def make_list_of_words(self):
        with open(f'{self.path}', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            lines = [line.rstrip('\n') for line in lines]
        return lines

    def get_list_of_words(self):
        return self.list_of_words

    def inf_for_training_frame(self):
        rand_task =choice(self.list_of_words).split('/')
        self.question = rand_task[0]
        self.answer = rand_task[1]



# l = training()
# a = Voc(l[0])
# print(a.question)
# print(a.answer)
# a.inf_for_training_frame()
# print(a.question)
# print(a.answer)