import os
import argparse
import glob
import logging

logger = logging.getLogger("yolo_class_id.log")
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename="yolo_class_id.log",
                    format='%(asctime)s : %(levelname)s %(message)s',
                    level=logging.DEBUG)


def change_class_id(txt_path, new_class_id):
    try:
        with open(txt_path, 'r') as f:
            lines = f.readlines()
            lines = [
                f"{new_class_id} {' '.join(line.split(' ')[1:])}"
                for line in lines
            ]
            logger.info(f"Changed class id in {txt_path}")
            with open(txt_path, 'w') as f:
                f.write('\n'.join(lines))
    except Exception as e:
        logger.error(f"An error occurred: {e}")


def change_class_id_in_folder(folder_path, new_class_id):
    try:
        file_paths = glob.glob(os.path.join(folder_path, '**', '*.txt'),
                               recursive=True)
        [change_class_id(file_path, new_class_id) for file_path in file_paths]
        return True
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return False
