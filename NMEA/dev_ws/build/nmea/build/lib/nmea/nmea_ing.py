import pyproj
import pynmea2
from std_msgs.msg import String

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

class Nmea:
    #nmea_data: String
    parsed_data: ParsedData
    
    #def __init__(self, nmea_data):
    def __init__(self): 
        #self.nmea_data = nmea_data 
        self.parsed_data = None
    
    def parsing(self):
        filename = '/home/user/Desktop/vilab/nmea.txt'
        with open(filename, 'r') as f:
            lines = f.readlines()

            for nmea_data in lines:
                if nmea_data[3:6] == "GGA":
                    line_list = nmea_data.split(',')
                    print("---------------GGA DATA----------------")

                    raw_data = nmea_data.strip()
                    message_id = line_list[0]
                    utc = line_list[1]

                    latitude, longitude = self.TM2UTM(nmea_data)

                    lat_dir = line_list[3]
                    lon_dir = line_list[5]
                    quality = line_list[6]
                    num_satellite = line_list[7]
                    hdop = line_list[8]
                    alt = line_list[9]
                    alt_unit = line_list[10]
                    sep = line_list[11]
                    sep_unit = line_list[12]
                    diff_age = line_list[13]
                    diff_station = line_list[14]

                    self.parsed_data = ParsedData(
                        raw_data, message_id, utc, latitude, lat_dir, longitude, lon_dir,
                        quality, num_satellite, hdop, alt, alt_unit, sep, sep_unit,
                        diff_age, diff_station
                    )

                    print(self.parsed_data)

            

    # Convert to UTM coordinate
    def TM2UTM(self, gga_sentence):
        # Parse GGA sentence
        msg = pynmea2.parse(gga_sentence)

        latitude = float(msg.latitude) if msg.lat_dir == 'N' else -float(msg.latitude)
        longitude = float(msg.longitude) if msg.lon_dir == 'E' else -float(msg.longitude)

        return latitude, longitude

# Example usage
#nmea_sentence = "$GNGGA,120048.80,3736.7136712,N,12659.6338670,E,5,12,0.74,113.391,M,18.444,M,0.8,0000*62"
n = Nmea()
n.parsing()
