
from typing import List, Any
from typing_extensions import TypedDict

class GGAParsedData(TypedDict, total=False):
    raw_data: str
    message_id: str
    utc: str
    latitude: float
    lat_dir: str
    longitude: float
    lon_dir: str
    quality: str
    num_satellite: str
    HDOP: str
    alt: str
    alt_unit: str
    sep: str
    sep_unit: str
    diff_age: str
    diff_station: str
