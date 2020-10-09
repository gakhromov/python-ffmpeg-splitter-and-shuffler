import os
import subprocess

from .time_parser import parse_time_file


def split(inp_audio_file, inp_time_file, dir, 
            time_mode='short'): # or full
    # get folder + file name
    file_name = os.path.basename(inp_audio_file).split('.')[0]

    if not os.path.exists(os.path.abspath(dir + '/tmp')):
        os.mkdir(dir + '/tmp')

    timecodes = parse_time_file(inp_audio_file, inp_time_file, time_mode)

    for i, (start, end) in enumerate(timecodes):
        end_file = dir + f'/tmp/{file_name}_{i}.mp3'
        subprocess.run(['ffmpeg', '-i', inp_audio_file , '-ss', start, '-to', end, end_file])
    
