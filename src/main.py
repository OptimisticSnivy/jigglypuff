import argparse
import os
from ffpyplayer.player import MediaPlayer
from pathlib import Path

files = []
file_formats = [".mp3", ".flac"]


# optimize it?
def walkDir(target_dir):
    for entry in target_dir.iterdir():
        if entry.suffix in file_formats:
            files.append(entry)
        elif os.path.isdir(entry):
            walkDir(entry)

    return files


def getQueue():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Add a path containing Music")

    args = parser.parse_args()
    target_dir = Path(args.path)
    files = walkDir(target_dir)

    playQueue(files)


def playQueue(files):
    for i in range(0, len(files)):
        print("Now Playing:-", files[i].name)
        player = MediaPlayer(str(files[i]))
        val = " "
        while val != "eof":
            frame, val = player.get_frame()
            if val != "eof" and frame is not None:
                img, t = frame


getQueue()
