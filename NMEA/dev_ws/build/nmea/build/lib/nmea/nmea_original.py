import pyproj
import pynmea2

class Nmea:
    filename : str
    
    def __init__(self, filename): 
        self.filename = filename 
    
    def info(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()

        for line in lines:
            if line[3:6] == "GGA":
                line_list = line.split(',')
                print("---------------GGA DATA----------------")
                print("GGA.raw_data :", line.strip())
                print("GGA.message_id :", line_list[0])
                print("GGA.utc :", line_list[1])

                latitude, longitude = self.TM2UTM(line)

                print("GGA.lat :", latitude)
                print("GGA.lat_dir :", line_list[3])
                print("GGA.lon :", longitude)
                print("GGA.lon_dir :", line_list[5])
                print("GGA.quality :", line_list[6])
                print("GGA.num_satelite :", line_list[7])
                print("GGA.HDOP :", line_list[8])
                print("GGA.alt :", line_list[9])
                print("GGA.alt_unit :", line_list[10])
                print("GGA.sep :", line_list[11])
                print("GGA.sep_unit :", line_list[12])
                print("GGA.diff_age :", line_list[13])
                print("GGA.diff_station :", line_list[14])
                #print("GGA.check_sum :", line_list[15])


    # Convert to UTM cordinate
    def TM2UTM(self, gga_sentence):
        # Parse GGA sentence
        msg = pynmea2.parse(gga_sentence)

        latitude = float(msg.latitude) if msg.lat_dir == 'N' else -float(msg.latitude)
        longitude = float(msg.longitude) if msg.lon_dir == 'E' else -float(msg.longitude)

        return latitude, longitude


n = Nmea('./nmea.txt')

n.info()
