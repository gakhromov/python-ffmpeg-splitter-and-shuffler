import os
import random


def shuffle(dir):
    files = os.listdir(os.path.abspath(dir + '/tmp'))
    random.shuffle(files)
    slsh = '/'

    # lines = [f"file '{os.path.abspath(dir + slsh + f_name)}'\n" for f_name in files]
    lines = [f"file '{f_name}'\n" for f_name in files]
    lines[-1] = lines[-1].rstrip() # remove \n at the end

    with open(os.path.abspath(dir+ '/tmp/list.txt'), 'w') as f:
        f.writelines(lines)
