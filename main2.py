from DataFrameHandler import DataFrameHandler
from MGRSConverter import MGRSConverter
from MGRSFormatter import MGRSFormatter


class main:

    def __init__(self, file_path):
        """ Initialise the main class to run the program.

        :param file_path: The .csv file to be converted.

        Attributes
        raw_data: raw .csv file
        coordinate_data: Data frame containing the initial "Latitude" and "Longitude" values
        mgrs_list: List containing the MGRS strings in the same order as the data frame
        latlon_list: List containing list of latitude and list of longitude.
        lat_list: List of revised Latitudes
        long_list: List of revised longitudes
        output_csv: output .csv file
        """

        self.raw_data = file_path
        self.coordinate_data = None
        self.mgrs_list = None
        self.latlon_list = None
        self.lat_list = None
        self.lon_list = None
        self.output_csv = None

    def read_csv(self):
        """ Call the method from DataFrameHandler to read the .csv file

        Updates coordinate_data with the Data frame
        """

        # print("start read")
        self.coordinate_data = DataFrameHandler.read_csv(self.raw_data)
        # print("end read")
        # print(self.coordinate_data)

    def format_mgrs(self):
        """ Call the method from MGRSFormatter with the initial data frame as an argument
         to format the values in the initial data frame into MGRS strings

        Updates the mgrs_list with a List of MGRS String values
        """

        # print("start format")
        self.mgrs_list = MGRSFormatter.mgrs_formatter(self.coordinate_data)
        # print(self.mgrs_list)
        # print("end format")

    def convert_mgrs(self):
        """ Call the method from MGRSConverter with the mgrs_list as the argument
         to convert the MGRS Strings into Coordinates

        Updates the latlon_list with a Pair of List of latitude and List of Longitude
        Updates the lat_list with a list of latitudes
        Updates the lon_list with a list of longitudes
        """

        # print("start convert")
        self.latlon_list = MGRSConverter.mgrs_converter(self.mgrs_list)
        self.lat_list_1 = self.latlon_list[0]
        self.lon_list_1 = self.latlon_list[1]
        self.lat_list_2 = self.latlon_list[2]
        self.lat_list_3 = self.latlon_list[3]
        # print(self.latlon_list)
        # print(self.lat_list)
        # print(self.lon_list)
        # print("end convert")

    def write_to_dataframe(self, data_frame, column_name, column_data):
        """ Call the method from DataFrameHandler to add the new column into the data frame

        :param data_frame: Data frame to add columns
        :param column_name: String name of column
        :param column_data: List of column data

        Updates the data_frame
        """
        DataFrameHandler.write_to_dataframe(data_frame, column_name, column_data)

    def write_csv(self):
        """ Call the method from DataFrameHandler with the data frame as an argument to create the .csv file

        Updates output_csv with the result
        """

        self.output_csv = DataFrameHandler.write_csv(self.coordinate_data)

    def run_whole_thing(self):
        """ Run the whole program to convert the latitude and longitude values in the .csv file and creates a
        new column with the converted latitude and longitude values

        Creates a new .csv file in the output folder
        """

        self.read_csv()
        self.format_mgrs()
        self.convert_mgrs()
        self.write_to_dataframe(self.coordinate_data, "MGRS", self.mgrs_list)
        self.write_to_dataframe(self.coordinate_data,"Revised_Latitude_1", self.lat_list_1)
        self.write_to_dataframe(self.coordinate_data, "Revised_Longitude_1", self.lon_list_1)
        self.write_to_dataframe(self.coordinate_data,"Revised_Latitude_2", self.lat_list_2)
        self.write_to_dataframe(self.coordinate_data, "Revised_Longitude_2", self.lon_list_2)
        self.write_csv()


if __name__ == '__main__':
    #Test run
    thisrun = main('input/Paths.csv')
    thisrun.run_whole_thing()