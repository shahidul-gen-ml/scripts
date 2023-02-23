# HTML generator

## For Help

```console
usage: html_generator.py [-h] [--video_folder VIDEO_FOLDER] [--file_name FILE_NAME] [--width WIDTH] [--height HEIGHT]

HTML generator For Videos Check

optional arguments:
  -h, --help            show this help message and exit
  --video_folder VIDEO_FOLDER, --vf VIDEO_FOLDER
                        path to folder with videos
  --file_name FILE_NAME, --fn FILE_NAME
                        name of the html file
  --width WIDTH, --w WIDTH
                        width of the video
  --height HEIGHT, --h HEIGHT
                        height of the video
```

### Example

```console
python html_generator.py --vf /media/shahidul/store1/generated_glosses/আজ --fn ottachar.html --w 320 --h 240
```

#### Example Folder Structure

```console
আছে
├── 1.mp4
├── 2.mp4
├── 3.mp4
না
├── 1.mp4
├── 2.mp4
├── 3.mp4
মানুষ
├── 1.mp4
├── 2.mp4
├── 3.mp4
```
