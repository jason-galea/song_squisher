#! python3

import sys, getopt, os, re, ffmpeg

from functions import *

def encode_mp3(filename, new_name): # str, int(seconds), int(seconds), str
    (
        ffmpeg.input(filename, **{
            # 'vsync':0 # Never allow duplicate frames
            # , 'hwaccel':'cuvid', 'c:v':'h264_cuvid' # Allow hwaccel with h264_cuvid decoder
        })
        .output(new_name, **{
            # 'c:v':'hevc_nvenc' # HEVC/H265 encoder
            # , 'ss':start_offset + 1, 't':duration # Trim start & restrict duration (AKA. trim end)
            # , 'rc:v':'vbr_hq', 'cq:v':19, 'preset':'slow' # Quality settings
            # , 'video_bitrate':'8M', 'audio_bitrate':'192K' # Bitrate settings (Audio still fluctuates, ehh)
            'audio_bitrate':'320K'
        })
        .overwrite_output() # Same as "-y"
        .run()
    )


cwd = os.getcwd()
os.chdir(cwd) # This avoids having to add "cwd" to the start of the filename/new_name(s)

print('>> This script will clean up any ".mp3" files in the current directory: "%s"' %(cwd))
input()

for filename in os.listdir(cwd):
    if ".flac" in filename:
        new_name = filename.replace(".flac", ".mp3")
        encode_mp3(filename, new_name)
    
    # exit() # Run only once

input("\n>> Press any key to exit")
exit()