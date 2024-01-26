class ParsedData:
    def __init__(self, raw_data, message_id, utc, 
    latitude, lat_dir, longitude, lon_dir, quality, 
    num_satellite, hdop, alt, alt_unit, sep, sep_unit, 
    diff_age, diff_station):
        self.raw_data = raw_data
        self.message_id = message_id
        self.utc = utc
        self.latitude = latitude
        self.lat_dir = lat_dir
        self.longitude = longitude
        self.lon_dir = lon_dir
        self.quality = quality
        self.num_satellite = num_satellite
        self.hdop = hdop
        self.alt = alt
        self.alt_unit = alt_unit
        self.sep = sep
        self.sep_unit = sep_unit
        self.diff_age = diff_age
        self.diff_station = diff_station

    def __str__(self):
        return (
            f"GGA.raw_data={self.raw_data},\n"
            f"GGA.message_id={self.message_id},\n"
            f"GGA.utc={self.utc},\n"
            f"GGA.latitude={self.latitude},\n"
            f"GGA.lat_dir={self.lat_dir},\n"
            f"GGA.longitude={self.longitude},\n"
            f"GGA.lon_dir={self.lon_dir},\n"
            f"GGA.quality={self.quality},\n"
            f"GGA.num_satellite={self.num_satellite},\n"
            f"GGA.HDOP={self.hdop},\n"
            f"GGA.alt={self.alt},\n"
            f"GGA.alt_unit={self.alt_unit},\n"
            f"GGA.sep={self.sep},\n"
            f"GGA.sep_unit={self.sep_unit},\n"
            f"GGA.diff_age={self.diff_age},\n"
            f"GGA.diff_station={self.diff_station}\n"
        )