import pandas as pd
import os

def getDf(fp):

    if os.path.exists(fp):

        return pd.read_csv(fp)

    print(f"File path does not exist: {fp}")
    
    return -1

if __name__ == "__main__":

    print("File is not meant for running..")