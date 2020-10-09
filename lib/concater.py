import os
import subprocess


def concatenate_files(dir):
    os.chdir(dir + '/tmp')
    lst = 'list.txt'
    out = '../out.mp3'
    print(lst, out)
    if os.path.exists(lst):
        subprocess.run(['ffmpeg', '-f', 'concat', '-i', lst, out])
    else:
        print('Error: Concat has not been done. (create list.txt in /tmp)')