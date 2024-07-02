from DataFrameHandler import DataFrameHandler
from MGRSConverter import MGRSConverter
from MGRSFormatter import MGRSFormatter


class main:

    def __init__(self, file_path):
        self.coordinate_data = file_path
        self.coordinate_list = None
        self.mgrs_list = None
        self.latlon_list = None

    def read_csv(self):
        print("start read")
        self.coordinate_list = DataFrameHandler.read_csv(self.coordinate_data)
        print("end read")
        print(self.coordinate_list)

    def format_mgrs(self):
        print("start format")
        self.mgrs_list = MGRSFormatter.mgrs_formatter(self.coordinate_list)
        print("end format")
        print(self.mgrs_list)

    def convert_mgrs(self):
        print("start convert")
        self.latlon_list = MGRSConverter.mgrs_converter(self.mgrs_list)
        print(self.latlon_list)

        print("end convert")

    def write_to_dataframe(self, data_frame, column_name, column_data):
        DataFrameHandler.write_to_dataframe(data_frame, column_name, column_data)

    def write_csv(self):
        DataFrameHandler.write_csv(self.coordinate_list)

    def run_whole_thing(self):
        self.read_csv()
        self.format_mgrs()
        self.convert_mgrs()
        self.write_to_dataframe(self.coordinate_list, "MGRS", self.mgrs_list)
        self.write_to_dataframe(self.coordinate_list, "Coordinates", self.latlon_list)
        self.write_csv()


if __name__ == '__main__':
    thisrun = main('input/Test.csv')
    thisrun.run_whole_thing()