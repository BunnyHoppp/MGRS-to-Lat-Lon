import pandas as pd


class MGRSFormatter:
    """Format Latitude, Longitude (from csv file) into MGRS.
    MGRS: Grid_Zone + 100,000 meter Square ID + 100 meter square

    Example (DALLAS deployment area):
        Latitude, Longitude (csv input): 101.5, 103.0
        MGRS: 56KKA015030

    Explanation:
        "56K" -> Grid Zone
        "KA" -> 100,000 meter Square ID (i.e., JA, KA, JV, KV)
            K: Latitude >100
            A: Longitude >100
        "015030" -> 100 meter square
            "015": Latitude 101.5 -> remove the first 1 (-100) and take out the decimal (*10)
            "030": Longitude 103

        Reference:
        https://mappingsupport.com/p2/gissurfer.php?center=14SQH05239974&zoom=4&basemap=USA_basemap
        https://www.maptools.com/tutorials/mgrs/quick_guide
    """

    Grid_Zone = "56K"
    Accuracy = 3
   
    @staticmethod
    def mgrs_formatter(dataframe):
        """
        Convert the Latitude and Longitude (csv input) to a list of mgrs_string
        using the helper function mgrs_tostring

        Args:
            dataframe: Latitude and Longitude (read from csv file)

        Returns:
            result: a list of mgrs_string
        """
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
        """ Convert 1 pair of latitude and longitude into 1 MGRS string using the helper function latlon_tostring.

        Args:
            latitude: Latitude value (top-down of map)
            longitude: Longitude value (left-right of map)

        Returns:
            result_string: MGRS string

        Steps to generate the output:
            1. Initialize result_string with the Grid Zone.
            2. Determine square_id (100,000 meter Square ID).
            3. Determine a string of numerical values representing the 100-meter square where the point lies using latlon_tostring.
               - Both latitude and longitude are evaluated individually.
            4. Add to result_string in this sequence: square_id, longitude, latitude.
               - Note: result_string is already initialized with Grid Zone from Step 1.
        """
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