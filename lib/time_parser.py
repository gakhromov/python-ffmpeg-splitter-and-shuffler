import subprocess
import datetime


def get_length(inp_audio_file):
    result = subprocess.run([
        'ffprobe', '-v', 'error', '-show_entries', 'format=duration', 
        '-of', 'default=noprint_wrappers=1:nokey=1', inp_audio_file
        ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    seconds = int(float(result.stdout))
    return str(datetime.timedelta(seconds=seconds))


def parse_time_file(inp_audio_file, inp_time_file, time_mode):
    # short mode: given only start timecode, without the end
    # full mode: given both start and end timecodes
    timecodes = []

    if time_mode == 'short':
        with open(inp_time_file, 'r', encoding='utf-8') as f:
            timecodes.append(['00:00', None])
            for line in f:
                timecodes[-1][1] = line.rstrip()
                timecodes.append([line.rstrip(), None])
            # remove the first 00 line
            timecodes.pop(0)
        
        timecodes[-1][1] = get_length(inp_audio_file)

    return timecodes
    