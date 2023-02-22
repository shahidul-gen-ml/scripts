import csv
import urllib.request
import os
import ssl
from tqdm import tqdm
import concurrent.futures

DOWNLOAD_PATH = 'DOWNLOAD_VIDEO1'

if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)

CSV_PATH = '/home/shahidul/Desktop/scripts/Training_Gloss_List_&_Details.xlsx - Gloss_Details.csv'

HEADER = [
    "idNumber", "annotationId", "attachmentId", "contentUrl", "fileName",
    "sentence", "sentenceId", "signSentence", "userId", "meta", "word",
    "start", "end"
]

for row in csv.DictReader(open(CSV_PATH)):
    url = row[HEADER[3]]
    filename = f'{DOWNLOAD_PATH}/{row[HEADER[4]]}'

ssl._create_default_https_context = ssl._create_unverified_context


def download_file(url, filename):
    urllib.request.urlretrieve(url, filename)


file_list = list(
    set([(row[HEADER[3]], f'{DOWNLOAD_PATH}/{row[HEADER[4]]}')
         for row in csv.DictReader(open(CSV_PATH))]))

with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count() *
                                           5) as executor:
    list(
        tqdm(executor.map(lambda x: download_file(*x), file_list),
             total=len(file_list)))
