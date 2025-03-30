import pandas as pd
import sys
from pathlib import Path

curDir = Path(__file__).resolve()
curDir = curDir.parent.parent
sys.path.insert(0, str(curDir))


import os
from constants import COLUMN_NAMES
from api.csvHandler import csvReader
from api.get_data import newData
from dotenv import load_dotenv

def getDf():

    # Returns movie dataset as a pandas dataframe

    data = csvReader()

    if not data:

        load_dotenv()

        API_KEY = os.getenv("API_KEY")

        newData(API_KEY, numPages=10)

        data = csvReader()
    
    df = pd.DataFrame(data, columns=COLUMN_NAMES)
    return df

if __name__ == "__main__":

    getDf()
    print("File is not meant for running..")