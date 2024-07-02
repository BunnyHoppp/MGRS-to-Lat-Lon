import pandas as pd


class CSV_reader:

    @staticmethod

    def read_csv(file_path):
        """Read the csv file and return a dataframe to be used in other classes 
    
        Args: 
            file_path: csv file containing the latitude/longitude derived from the map 

        Returns: 
            data_frame
        """
        data_frame = pd.read_csv(file_path)
        return data_frame
