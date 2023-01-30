import os
import argparse
import glob
import logging
try:
    from tqdm import tqdm
except ModuleNotFoundError:
    print("You need to install tqdm. Run: pip install tqdm")

logger = logging.getLogger("yolo_class_id.log")
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename="yolo_class_id.log",
                    format='%(asctime)s : %(levelname)s %(message)s',
                    level=logging.DEBUG)

parser = argparse.ArgumentParser(
    description='Change class id in yolo txt files')
parser.add_argument('--new_class_id', type=int, help='new class id')
parser.add_argument('--folder_path',
                    type=str,
                    help='path to folder with txt files')

args = parser.parse_args()


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


if __name__ == '__main__':
    try:
        file_paths = glob.glob(os.path.join(args.folder_path, '**', '*.txt'),
                               recursive=True)
        [
            change_class_id(file_path, args.new_class_id)
            for file_path in tqdm(file_paths)
        ]
    except Exception as e:
        logger.error(f"An error occurred: {e}")

# Run:
# python yolo_class_id.py --new_class_id 5 --folder_path /home/shahidul/Desktop/scripts/lol
