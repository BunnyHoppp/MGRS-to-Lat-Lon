import pandas as pd


class CSV_reader:

    @staticmethod
    def read_csv(file_path):
        data_frame = pd.read_csv(file_path)
        return data_frame