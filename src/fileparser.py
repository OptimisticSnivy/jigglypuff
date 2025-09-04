import argparse
from pathlib import Path

file_formats = [ ".mp3", ".flac"]
parser = argparse.ArgumentParser()
parser.add_argument("path", help="Add a path containing Music")

args = parser.parse_args()
target_dir = Path(args.path)

for entry in target_dir.iterdir():
    if entry.suffix in file_formats:
        print(entry)
