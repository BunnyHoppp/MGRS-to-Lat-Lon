import pandas as pd 

class CSVToDataFrame:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data_frame = None
    
    def read_csv(self):
        self.data_frame = pd.read_csv(self.file_path)
    
    def display(self):
        if self.data_frame is not None:
            print(self.data_frame.head())

csv_to_df = CSVToDataFrame('Wallaby Medium Input 1.csv')
csv_to_df.read_csv()
csv_to_df.display()

