from logic_for_training import training, Voc, get_path
import os, os.path


l = Voc("new")

for i in l.list_of_words:
    hanzi_name = i.split('/')[0]
    w = i.split('/')[1]
    pinin_name = w.split(maxsplit=1)[0]
    translstion_name = w.split(maxsplit=1)[1]
    with open(os.path.join(get_path(), 'words', "new2"), "a", encoding="utf-8") as file:
        file.write(''.join([translstion_name,'/', hanzi_name," ", pinin_name]) + "\n")


# with open(os.path.join(get_path(), 'words', new_file_name), "a", encoding="utf-8") as file:
#     file.write(''.join([hanzi_name,'/', pinin_name," ", translstion_name]) + "\n")
#