import argparse
from ffpyplayer.player import MediaPlayer
from pathlib import Path

file_formats = [".mp3", ".flac"]
files = []
parser = argparse.ArgumentParser()
parser.add_argument("path", help="Add a path containing Music")

args = parser.parse_args()
target_dir = Path(args.path)

for entry in target_dir.iterdir():
    if entry.suffix in file_formats:
        files.append(str(entry))

print(files)
player = MediaPlayer(files[0])
val = " "
while val != "eof":
    frame, val = player.get_frame()
    if val != "eof" and frame is not None:
        img, t = frame
