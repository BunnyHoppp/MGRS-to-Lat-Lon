import mgrs


class MGRSConverter:
    """ Convert MGRS to (Lat,Lon)

    Attributes:
        mgrs_obj: the mgrs object initialised.

    Convert mgrs (string) into mgrs_obj
    """

    mgrs_obj = mgrs.MGRS()

    @staticmethod
    def mgrs_converter(mgrs_list):
        """Convert a List of MGRS coordinates to a List of (Latitude, Longitude) using a helper function mgrs_tolatlon

        Args:
            mgrs_list: a List of MGRS coordinates

        Returns:
            result_list: a List of (Latitude, Longitude)
        """

        list_len = len(mgrs_list)
        result_list = list()
        for i in range(list_len):
            mgrs_string = mgrs_list[i]
            latlon_pair = MGRSConverter.mgrs_tolatlon(mgrs_string)
            result_list.append(latlon_pair)
        return result_list

    @staticmethod
    def mgrs_tolatlon(mgrs_string):
        """Convert 1 mgrs_string to 1 (Latitude, Longitude)

        Args:
            mgrs_string: MGRS Coordinate

        Returns:
            result: (Latitude, Longitude)
        """

        if mgrs_string == None:
            return None
        result = MGRSConverter.mgrs_obj.toLatLon(mgrs_string)
        return result