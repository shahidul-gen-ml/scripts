#Example: python html_generator.py --vf /media/shahidul/store1/generated_glosses/আজ --fn ottachar.html --w 320 --h 240

import os
import argparse

parser = argparse.ArgumentParser(description='HTML generator For Videos Check')
parser.add_argument('--video_folder',
                    '--vf',
                    type=str,
                    help='path to folder with videos')
parser.add_argument('--file_name',
                    '--fn',
                    type=str,
                    default='index.html',
                    help='name of the html file')
parser.add_argument('--width',
                    '--w',
                    default=320,
                    type=int,
                    help='width of the video')
parser.add_argument('--height',
                    '--h',
                    default=240,
                    type=int,
                    help='height of the video')

args = parser.parse_args()

VIDEO_FOLDER = args.video_folder
FILENAME = args.file_name
WIDTH = args.width
HEIGHT = args.height

html_start = '<!DOCTYPE html><html><head>    <title>Cheking Video</title>    <style>        .video-container {            display: flex;            flex-direction: row;            flex-wrap: wrap;        }       .video-container video {            margin-right: 10px;        }    </style></head><body>    <div class="video-container">'

with open(FILENAME, 'w') as f:
    f.write(html_start)

# list all files in the folder with path
files = [
    os.path.join(VIDEO_FOLDER, f) for f in os.listdir(VIDEO_FOLDER)
    if os.path.isfile(os.path.join(VIDEO_FOLDER, f))
]

# generate a index.html file with the list of files and play videos
for file in files:
    filename = os.path.basename(file)
    with open(FILENAME, 'a') as f:
        f.write(
            f'<div>            <h4>{filename}</h4>            <video width={WIDTH} height={HEIGHT} controls>                <source src={file} type="video/mp4">            </video>        </div>'
        )

html_end = '</div></body></html>'
with open(FILENAME, 'a') as f:
    f.write(html_end)
