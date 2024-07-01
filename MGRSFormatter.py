import math


class MGRSFormatter:

    """
    Purpose: Formatting our Latitude, Longitude read from the given map (data from csv file) into MGRS. 
    MGRS: Grid_Zone + 100,000 meter Square ID + Numerical Coordinates 
    
    Using DALLAS as a deployment area as an example: 
        Latitude, Longitude read from the given map (data from csv file): 101.5, 103.0 
        MGRS: 56KKA015030 

    Explanation: 
        "56K" -> Grid Zone  
        "KA" -> 100,000 meter Square ID 
            we are focusing on the 4 Square IDs: JA, KA, JV, KV  
            K: Latitude >100 
            A: Longitude >100
        "015030" -> Further zoomed in more within a 100 meter square (Numerical Coordinates) 
            "015": Latitude 101.5 -> remove the first 1 (-100) and take out the decimal (*10)    
            "030": Longitude 103                
        
        Reference: 
        https://mappingsupport.com/p2/gissurfer.php?center=14SQH05239974&zoom=4&basemap=USA_basemap
        https://www.maptools.com/tutorials/mgrs/quick_guide                
    """

    """
    MGRS: "Grid_Zone" + "100,000 meter Square ID" + "Numerical Coordinates" 
    """
    
    """
    mgrs_string (already added): None 
    mgrs_string (to add): "Grid_Zone"
    """
    Grid_Zone = "56K"
   
    @staticmethod
    """
    mgrs_string (already added): "Grid_Zone" 
    mgrs_string (to add): "Grid_Zone"
    """
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
        if value >= 100:
            value -= 100
            value *= 10
        else:
            value *= 10
        result = str(int(value))
        while True:
            if len(result) < 3:
                result = "0" + result
            else:
                break
        return result
