import pandas as pd


class MGRSFormatter:
    Grid_Zone = "56K"

    @staticmethod
    def mgrs_formatter(dataframe):
        number_of_points = dataframe.len()
        result = list()
        for i in range(number_of_points):
            latitude = dataframe.loc[i, 'Latitude']
            longitude = dataframe.loc[i, 'Longitude']
            mgrs_string = MGRSFormatter.mgrs_tostring(latitude, longitude)
            result.append(mgrs_string)
        return result

    @staticmethod
    def mgrs_tostring(latitude, longitude):
        result_string = MGRSFormatter.Grid_Zone
        square_id = ""
        if longitude >= 100:
            square_id += "K"
        else:
            square_id += "J"

        if latitude >= 100:
            square_id += "A"
        else:
            square_id += "V"
        latitude = MGRSFormatter.latlon_tostring(latitude)
        longitude = MGRSFormatter.latlon_tostring(longitude)
        result_string += longitude
        result_string += latitude
        return result_string

    @staticmethod
    def latlon_tostring(value):
        if value > 100:
            value -= 100
            value *= 10
        else:
            value *= 10
        return str(value)