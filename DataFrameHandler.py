import pandas as pd
import datetime


class DataFrameHandler:
    OUTPUT_ID = 0
    @staticmethod
    def read_csv(file_path):
        data_frame = pd.read_csv(file_path)
        if "Latitude" not in data_frame.columns:
            raise Exception("Latitude not present in this file")
        if "Longitude" not in data_frame.columns:
            raise Exception("Longitude not present in this file")
        return data_frame

    @staticmethod
    def write_csv(data_frame):
        csv = data_frame.to_csv(f"output/Output - {datetime.date.today()}.csv")
        DataFrameHandler.OUTPUT_ID += 1
        return csv

    @staticmethod
    def write_to_dataframe(data_frame, column_name, column_data):
        data_frame.loc[:, column_name] = column_data
        return data_frame