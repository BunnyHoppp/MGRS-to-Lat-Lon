from CSV_reader import CSV_reader
from MGRSConverter import MGRSConverter
from MGRSFormatter import MGRSFormatter
class main:

    def __init__(self, file_path):
        """ Initialisation 

        Args: 
            file_path: csv file  
        """
        self.coordinate_data = file_path
        self.coordinate_list = None
        self.mgrs_list = None
        self.latlon_list = None

    def read_csv(self):
        """ read the csv file containing latitude/longitude (top to bottom/ left to right in map)  
        """
        print("start read")
        self.coordinate_list = CSV_reader.read_csv(self.coordinate_data)
        print("end read")
        print(self.coordinate_list)

    def format_mgrs(self):
        """format the lat/lon (top to bottom / left to right in map) into appropriate mgrs format  
        """
        print("start format")
        self.mgrs_list = MGRSFormatter.mgrs_formatter(self.coordinate_list)
        print("end format")
        print(self.mgrs_list)

    def convert_mgrs(self):
        """convert mgrs to latitude/longitude
        """
        print("start convert")
        self.latlon_list = MGRSConverter.mgrs_converter(self.mgrs_list)
        print(self.latlon_list)

        print("end convert")

    def run_whole_thing(self):
        """ run everything: lat/lon in csv -> mgrs -> latitude/longitude 
        """
        self.read_csv()
        self.format_mgrs()
        self.convert_mgrs()
        self.coordinate_list ["latlon_list"] = self.latlon_list
        print(self.coordinate_list)

if __name__ == '__main__':
    """run     
    """
    thisrun = main('Test.csv')
    thisrun.run_whole_thing()
