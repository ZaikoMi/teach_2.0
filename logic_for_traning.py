from collections.abc import list_iterator
from random import choice
import os, os.path

def Training():
    current_dir = os.path.dirname(__file__)
    path =  os.path.join(current_dir, 'words')
    all_files = os.listdir(path)
    list_of_files = []
    for num, name in enumerate(all_files):
        list_of_files.append(f'{num+1}: {name}')
    return list_of_files


print(Training())

