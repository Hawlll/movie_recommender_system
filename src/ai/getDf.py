import pandas as pd
import os
from src.constants import COLUMN_NAMES

def getDf(fp):

    # Returns movie dataset as a pandas dataframe

    if os.path.exists(fp):

        return pd.read_csv(fp, names=COLUMN_NAMES)

    print(f"File path does not exist: {fp}")
    
    return -1

if __name__ == "__main__":

    print("File is not meant for running..")