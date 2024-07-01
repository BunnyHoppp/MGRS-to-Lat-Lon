import mgrs


class MGRSConverter:
    mgrs_obj = mgrs.MGRS()

    @staticmethod
    def mgrs_converter(mgrs_list):
        list_len = len(mgrs_list)
        result_list = list()
        for i in range(list_len):
            mgrs_string = mgrs_list[i]
            latlon_pair = MGRSConverter.mgrs_tolatlon(mgrs_string)
            result_list.append(latlon_pair)
        return result_list

    @staticmethod
    def mgrs_tolatlon(mgrs_string):
        result = MGRSConverter.mgrs_obj.toLatLon(mgrs_string)
        return result