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

    Precision:
    10,000m - 56K KV 1 1
    1000m   - 56K KV 10 10
    100m    - 56K KV 120 340
    10m     - 56K KV 1233 3453
    1m      - 56K KV 12343 45673

    Static Attributes:
    Grid_zone: This is the first 3 characters of the MGRS String. 56K is standard for the relevant map
    Accuracy: This shows the number of characters we need for the values in the last 2 segments of the MGRS String
    Accuracy of 3 means the precision is at 100m. Eg of MGRS String is 56K KV 120 340.


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
            3. Determine a string of numerical values representing the 100-meter square where the point lies
                using latlon_tostring.
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
        """
        Args:
            value: latitude/longitude derived from map
        Returns:
            result: numerical values which represent the 100 meter square that the point lies in
        Steps to generate the output:
            - if value > 100, -100
            - *10 to resulting value
            - if resulting value <10.0 ("100"), for example value = 5 ("50")

        Example: converting 101.5 to "015"
            - 101.5 - 100 = 1.5
            - 1.5 * 10 = 15 (not in the required format)
            - convert to string: 15 -> "15"
            - "0" + "15" = "015"
        """
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