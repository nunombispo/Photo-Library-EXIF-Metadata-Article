import os
import csv
from pathlib import Path
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

def extract_metadata(image_path):
    """Extract filename, timestamp, GPS coordinates, altitude, and camera info."""
    with open(image_path, 'rb') as img_file:
        img = Image(img_file)

    # Filename
    filename = Path(image_path).name

    # Timestamp
    timestamp = getattr(img, "datetime_original", "Unknown")

    # Camera model
    camera = getattr(img, "model", "Unknown")

    # GPS data - convert to decimal degrees
    lat = convert_to_decimal_degrees(
        getattr(img, "gps_latitude", None),
        getattr(img, "gps_latitude_ref", "N")
    )
    lon = convert_to_decimal_degrees(
        getattr(img, "gps_longitude", None),
        getattr(img, "gps_longitude_ref", "E")
    )
    
    # Altitude
    alt = getattr(img, "gps_altitude", None)
    if alt is not None and getattr(img, "gps_altitude_ref", 0) == 1:
        alt = -alt  # below sea level

    return {
        "filename": filename,
        "timestamp": str(timestamp),
        "latitude": lat,
        "longitude": lon,
        "altitude": alt,
        "camera": str(camera),
    }

def build_index(photo_dir, output_csv="photo_index.csv"):
    """Build an index of photos with their metadata"""
    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["filename", "timestamp", "latitude", "longitude", "altitude", "camera"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for root, _, files in os.walk(photo_dir):
            for file in files:
                if file.lower().endswith((".jpg", ".jpeg", ".tiff")):
                    try:
                        metadata = extract_metadata(os.path.join(root, file))
                        writer.writerow(metadata)
                        print(f"Processed: {file}")
                    except Exception as e:
                        print(f"Failed to process {file}: {e}")

# Example usage - process current directory
print("Building photo index from current directory...")
build_index("photos")
print("Photo index created successfully!")