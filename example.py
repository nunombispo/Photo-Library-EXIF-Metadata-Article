from exif import Image

def convert_to_decimal_degrees(gps_coord, ref):
    """Convert GPS coordinates from (degrees, minutes, seconds) to decimal degrees"""
    if gps_coord is None:
        return None
    
    degrees, minutes, seconds = gps_coord
    decimal_degrees = degrees + (minutes / 60.0) + (seconds / 3600.0)
    
    # Apply negative sign based on reference
    if ref in ['S', 'W']:
        decimal_degrees = -decimal_degrees
    
    return decimal_degrees

def get_gps_from_image(image_path):
    with open(image_path, 'rb') as img_file:
        img = Image(img_file)

    if not img.has_exif or not img.gps_latitude or not img.gps_longitude:
        return None  # No GPS data available

    # Convert to decimal degrees
    lat = convert_to_decimal_degrees(img.gps_latitude, img.gps_latitude_ref)
    lon = convert_to_decimal_degrees(img.gps_longitude, img.gps_longitude_ref)

    # Get altitude if available
    alt = img.gps_altitude if hasattr(img, 'gps_altitude') else None
    if alt is not None and hasattr(img, 'gps_altitude_ref') and img.gps_altitude_ref == 1:
        alt = -alt  # Altitude reference 1 = below sea level

    return (lat, lon, alt)

# Example usage
print(get_gps_from_image("england-london-bridge.jpg"))
