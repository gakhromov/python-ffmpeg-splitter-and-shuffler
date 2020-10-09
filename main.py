import os
import argparse as argp

from lib.splitter import split
from lib.shuffler import shuffle
from lib.concater import concatenate_files


def split_mode(args):
    audio_files = sorted(os.listdir(args.dir + '/audio'))
    time_files = sorted(os.listdir(args.dir + '/time'))

    for audio, timecode in zip(audio_files, time_files):
        abs_audio = os.path.abspath(args.dir + '/audio/' + audio)
        abs_timecode = os.path.abspath(args.dir + '/time/' + timecode)

        if os.path.exists(abs_audio) and os.path.exists(abs_timecode):
            split(abs_audio, abs_timecode, os.path.abspath(args.dir))
    
    print('************************')
    print('* Splitting completed! *')
    print('************************')


def shuffle_mode(args):
    shuffle(os.path.abspath(args.dir))
    print('************************')
    print('* Shuffling completed! *')
    print('************************')


def concat_mode(args):
    concatenate_files(os.path.abspath(args.dir))
    print('************************')
    print('* Concating completed! *')
    print('************************')


if __name__ == "__main__":
    parser = argp.ArgumentParser()
    parser.add_argument('-m', '--mode', nargs='+', help='Program mode (split, shuffle or concat)', required=True)
    parser.add_argument('-d', '--dir', type=str, help='Working directory', required=True)

    args = parser.parse_args()
    if 'split' in args.mode: split_mode(args)
    if 'shuffle' in args.mode: shuffle_mode(args)
    if 'concat' in args.mode: concat_mode(args)
