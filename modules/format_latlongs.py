def trunc_round(num, precision=3):
    parts = (str(num).split('.'))
    if len(parts) < 2:
        return (str(num) + '.' + ('0' * precision)) # no decimal part
    
    integer = parts[0]
    decimal = parts[1][:precision]
    if len(decimal) < precision:
        decimal = decimal + ('0' * (precision - len(decimal)))
    return (integer + '.' + decimal)

# print(trunc_round(lat_dms[2], 6), trunc_round(lon_dms[2], 6))
# print(trunc_round(60, 6), trunc_round(60.0, 6))


def latlon_to_dms(lat, lon):
    '''Converts lat_new to DMS precise format (degrees, minutes, seconds)'''
    def to_dms(value):
        degrees = int(value)
        minutes_full = abs((value - degrees) * 60)
        minutes = int(minutes_full)
        seconds = (minutes_full - minutes) * 60
        return degrees, minutes, seconds

    lat_deg, lat_min, lat_sec = to_dms(lat)
    lon_deg, lon_min, lon_sec = to_dms(lon)

    return (f"{lat_deg}°{lat_min}'{trunc_round(lat_sec, 2)}"), (f"{lon_deg}°{lon_min}'{trunc_round(lon_sec, 2)}")

# lat_dms, lon_dms = latlon_to_dms(67.99999682172047, 22.499998619459987)
# print("New lat DMS:", lat_dms)
# print("New lon DMS:", lon_dms)


def latlon_to_decimal_minutes(lat, lon):
    '''Converts lat_new to Decimal Minutes format'''
    def to_decimal_minutes(value):
        degrees = int(value)
        minutes_full = abs((value - degrees) * 60)
        return degrees, minutes_full

    lat_deg, lat_min = to_decimal_minutes(lat)
    lon_deg, lon_min = to_decimal_minutes(lon)

    return (f'{lat_deg}°{trunc_round(lat_min,3)}'), (f'{lon_deg}°{trunc_round(lon_min,3)}')

# lat_dm, lon_dm = latlon_to_decimal_minutes(67.99999682172047, 22.499998619459987)
# print("New lat Decimal Minutes:", lat_dm)
# print("New lon Decimal Minutes:", lon_dm)
