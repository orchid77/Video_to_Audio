# coding = utf-8
from moviepy.editor import AudioFileClip
import sys

source_path=sys.argv[1]
destination_path=sys.argv[2]

print(source_path)
print(destination_path)

my_audio_clip = AudioFileClip(source_path)
my_audio_clip.write_audiofile(destination_path)