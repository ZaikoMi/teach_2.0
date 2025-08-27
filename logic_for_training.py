from random import choice
import os, os.path



def get_path():
    return os.path.dirname(__file__)

def training():

    path =  os.path.join(get_path(), 'words')
    all_files = os.listdir(path)
    list_of_files = []
    for f_name in all_files:
        list_of_files.append(f_name)
    return list_of_files

class Voc:
    def __init__(self, name):
        self.path = os.path.join(get_path(), 'words', name)
        self.list_of_words = self.make_list_of_words()
        self.question = None
        self.previous_question = None
        self.answer_hanzi = ''
        self.previous_hanzi = " "
        self.answer_pinin = ''


    def make_list_of_words(self):
        with open(f'{self.path}', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            lines = [line.rstrip('\n') for line in lines]
        return lines

    def get_list_of_words(self):
        return self.list_of_words

    def inf_for_training_frame(self):
        self.previous_question = self.question
        self.previous_hanzi = self.answer_hanzi
        rand_task =choice(self.list_of_words).split('/')
        full_answer = rand_task[1].split(maxsplit=1)
        self.question = rand_task[0]
        self.answer_hanzi = full_answer[0]
        self.answer_pinin = full_answer[1]



# l = training()
# a = Voc(l[0])
# print(a.question)
# print(a.answer)
# a.inf_for_training_frame()
# print(a.question)
# print(a.answer)