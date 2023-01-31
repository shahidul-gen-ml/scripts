import os
from data_allign import get_id_from_class_name
from yolo_class_id_modified import change_class_id_in_folder
from argparse import ArgumentParser
try:
    from tqdm import tqdm
except ModuleNotFoundError:
    print("You need to install tqdm. Run: pip install tqdm")

parser = ArgumentParser()
parser.add_argument("-f",
                    "--folder_path",
                    help="Folder path to change class id")
args = parser.parse_args()

FOLDER_PATH = args.folder_path
if not FOLDER_PATH:
    print("Please provide folder path to change class id")
    exit()

AVAILABLE_CLASSES = os.listdir(FOLDER_PATH)

[
    change_class_id_in_folder(os.path.join(FOLDER_PATH, name),
                              get_id_from_class_name(name))
    for name in tqdm(AVAILABLE_CLASSES)
]
