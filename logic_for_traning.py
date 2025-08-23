from collections.abc import list_iterator
from random import choice
import os, os.path

def Training():
    current_dir = os.path.dirname(__file__)
    path =  os.path.join(current_dir, 'words')
    all_files = os.listdir(path)
    list_of_files = []
    for f_name in all_files:
        list_of_files.append(f_name)
    return list_of_files


print(Training())

