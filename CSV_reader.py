import pandas as pd


class CSV_reader:

    @staticmethod

    """
    Read the csv file and return a dataframe to be used in the subsequent classes 
    """
    
    def read_csv(file_path):
        data_frame = pd.read_csv(file_path)
        return data_frame
