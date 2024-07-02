import math


class MGRSFormatter:

    """
    Purpose: Formatting our Latitude, Longitude read from the given map (data from csv file) into MGRS. 
    MGRS: Grid_Zone + 100,000 meter Square ID + 100 meter square  
    
    Using DALLAS as a deployment area as an example: 
        Latitude, Longitude read from the given map (data from csv file): 101.5, 103.0 
        MGRS: 56KKA015030 

    Explanation: 
        "56K" -> Grid Zone  
        "KA" -> 100,000 meter Square ID 
            we are focusing on the 4 Square IDs: JA, KA, JV, KV  
            K: Latitude >100 
            A: Longitude >100
        "015030" -> Further zoomed in more within a 100 meter square 
            "015": Latitude 101.5 -> remove the first 1 (-100) and take out the decimal (*10)    
            "030": Longitude 103                
        
        Reference: 
        https://mappingsupport.com/p2/gissurfer.php?center=14SQH05239974&zoom=4&basemap=USA_basemap
        https://www.maptools.com/tutorials/mgrs/quick_guide                
    """
  
    Grid_Zone = "56K"
   
    @staticmethod
    def mgrs_formatter(dataframe):
        """ 
        Converts the Latitude and Longitude in the dataframe (read from csv file) to a list of mgrs_string 
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
        """
        Convert 1 pair of latitude and longitude to 1 result_string 
        using the helper function latlon_tostring.    
        
        Agrs: 
            latitude: top-down of map  
            longitude: left-right of map 
        Returns: 
            result_string: mgrs_string 

        From Args, how do we get our output?: 
            1. Initialise result_string using Grid_Zone.  
            2. Evaluate the square_id 
                square_id: 100,000 meter Square ID
            3. Find a string of numerical values which represent the 100 meter square that the point lies in 
                using a helper function latlon_tostring 
                latitude and longitude is evaluated individually.  
            4. To result_string, add in this sequence: square_id, longitude, latitude.   
                Note that result_string already contained Grid_Zone which was already initialised in Step 1.
        """
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

    """
        Args: 
            value: latitude/longitude derived from the map 
        Returns: 
            result: numerical values which represent the 100 meter square that the point lies in 
        From Args, how do we get our output?: Example: converting 101.5 to "015"
        - remove the first 1 (-100), if any 
        -  remove the decimal (*10) 
        - at this point, we could end up having a value <10.0 ("100"), for example value = 5 ("50")  
           -> Example: 101.5 
              - 101.5 - 100 = 1.5 
              - 1.5 * 10 = 15 (not in the required format) 
             - convert to string: 15 -> "15" 
              - "0" + "15" = "015"  
        """
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
