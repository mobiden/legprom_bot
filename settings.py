import os
from datetime import datetime
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # абсолютный путь к директории проекта
BOT_TOKEN = '7004372053:AAHxBq1x2QohJQMGFMCByWKmsjOAQRaGX3k' # в продакте такую информацию надо прятать.


def create_logs(string: str, printing = False):
    with open("logs.txt", "a", encoding='utf-8') as l:
        string = str(datetime.now()) + ": " + string
        l.write(str(string) + "\n")
    if printing:
        print(string)

CSV_PATH = BASE_DIR + '\\CFN.csv'
TXT_PATH = BASE_DIR + '\\feat_list.txt'
COMP_FEAT_LIST = []
with open(TXT_PATH, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        temp_feat =[int(i) for i in line.split()]
        COMP_FEAT_LIST.append(temp_feat)



#COMP_FEAT = np.genfromtxt(CSV_PATH, dtype=None, delimiter=";", skip_header=0,
                             # encoding='utf-8', usecols=np.arange(0,3)                               )
#COMP_FEAT_LIST = COMP_FEAT.tolist()