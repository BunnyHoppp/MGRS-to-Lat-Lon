import pandas as pd


class MGRSFormatter:
    Grid_Zone = "56K"
    Accuracy = 3
   
    @staticmethod
    def mgrs_formatter(dataframe):
        number_of_points = len(dataframe)
        result = list()
        for i in range(number_of_points):
            latitude = dataframe.loc[i, 'Latitude']
            longitude = dataframe.loc[i, 'Longitude']
            mgrs_string = MGRSFormatter.mgrs_tostring(latitude, longitude)
            result.append(mgrs_string)
        return result

    @staticmethod
    def mgrs_tostring(latitude, longitude):
        if pd.isna(latitude) or pd.isna(longitude):
            return None
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
        result_string += square_id
        result_string += longitude
        result_string += latitude
        return result_string

    @staticmethod
    def latlon_tostring(value):
        decimal_points = MGRSFormatter.Accuracy - 2
        result_int = value
        if result_int >= 100:
            result_int -= 100
        result_int *= (pow(10, decimal_points))
        result = str(int(result_int))
        while True:
            if len(result) < MGRSFormatter.Accuracy:
                result = "0" + result
            else:
                break
        return result