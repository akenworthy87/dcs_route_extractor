def trunc_round(num, precision=3):
    parts = (str(num).split('.'))
    if len(parts) < 2:
        return (str(num) + '.' + ('0' * precision)) # no decimal part
    
    integer = f'{parts[0]:0>2}' # pad with leading zeros to ensure 2 digits
    decimal = parts[1][:precision]
    if len(decimal) < precision:
        decimal = decimal + ('0' * (precision - len(decimal)))
    return (integer + '.' + decimal)

# print(trunc_round(lat_dms[2], 6), trunc_round(lon_dms[2], 6))
# print(trunc_round(60, 6), trunc_round(60.0, 6))

def northing_easting(degrees: int, lat_or_lon: str) -> str:
    '''Works out if the degrees are north/south or east/west and returns the appropriate letter'''
    
    abs_degrees = abs(degrees)
    match lat_or_lon:
        case 'lat':
            if degrees >= 0:
                return f'N {abs_degrees}'
            else:
                return f'S {abs_degrees}'
        case 'lon':
            if degrees >= 0:
                return f'E {abs_degrees}'
            else:
                return f'W {abs_degrees}'
        case _:
            raise ValueError("lat_or_lon must be 'lat' or 'lon'")

def latlon_to_dms(lat, lon):
    '''Converts lat_new to DMS precise format (degrees, minutes, seconds)'''
    def to_dms(value, lat_or_lon):
        degrees = int(value)
        minutes_full = abs((value - degrees) * 60)
        minutes = int(minutes_full)
        seconds = (minutes_full - minutes) * 60
        return northing_easting(degrees, lat_or_lon), f'{minutes:0>2}', seconds

    lat_deg, lat_min, lat_sec = to_dms(lat, lat_or_lon='lat')
    lon_deg, lon_min, lon_sec = to_dms(lon, lat_or_lon='lon')
    
    # lat_deg = northing_easting(lat_deg, 'lat')
    # lon_deg = northing_easting(lon_deg, 'lon')

    return (f"{lat_deg}°{lat_min}'{trunc_round(lat_sec, 2)}\""), (f"{lon_deg}°{lon_min}'{trunc_round(lon_sec, 2)}\"")

# lat_dms, lon_dms = latlon_to_dms(67.99999682172047, 22.499998619459987)
# print("New lat DMS:", lat_dms)
# print("New lon DMS:", lon_dms)


def latlon_to_decimal_minutes(lat, lon):
    '''Converts lat_new to Decimal Minutes format'''
    def to_decimal_minutes(value, lat_or_lon: str):
        degrees = int(value)
        minutes_full = abs((value - degrees) * 60)
        return northing_easting(degrees, lat_or_lon), minutes_full

    lat_deg, lat_min = to_decimal_minutes(lat, lat_or_lon='lat')
    lon_deg, lon_min = to_decimal_minutes(lon, lat_or_lon='lon')
    
    # lat_deg = northing_easting(lat_deg, 'lat')
    # lon_deg = northing_easting(lon_deg, 'lon')

    return (f"{lat_deg}°{trunc_round(lat_min,3)}'"), (f"{lon_deg}°{trunc_round(lon_min,3)}'")

# lat_dm, lon_dm = latlon_to_decimal_minutes(67.99999682172047, 22.499998619459987)
# print("New lat Decimal Minutes:", lat_dm)
# print("New lon Decimal Minutes:", lon_dm)
