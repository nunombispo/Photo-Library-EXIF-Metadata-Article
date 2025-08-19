import math
import csv

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points on Earth's surface
    using the Haversine formula.
    
    Args:
        lat1, lon1: Latitude and longitude of first point (in decimal degrees)
        lat2, lon2: Latitude and longitude of second point (in decimal degrees)
    
    Returns:
        Distance in kilometers between the two points
    
    Formula: d = R * c
    where R is Earth's radius and c is the angular distance in radians
    """
    R = 6371  # Earth's radius in kilometers
    
    # Convert latitude and longitude from degrees to radians
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    
    # Calculate differences in latitude and longitude (in radians)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    # Haversine formula components:
    # a = sin²(Δφ/2) + cos(φ1) * cos(φ2) * sin²(Δλ/2)
    a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    
    # c = 2 * atan2(√a, √(1-a)) - angular distance in radians
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Final distance = Earth radius * angular distance
    return R * c

# Define the target location (London, UK coordinates)
target_lat, target_lon = 51.5074, -0.1278  # London coordinates in decimal degrees

# Set the search radius in kilometers
radius_km = 10

# Open and read the photo index CSV file
with open("photo_index.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)  # Read CSV as dictionary with column headers as keys
    
    # Process each row (photo) in the CSV file
    for row in reader:
        # Check if both latitude and longitude data exist for this photo
        if row["latitude"] and row["longitude"]:
            # Calculate distance from target location to photo location
            dist = haversine(target_lat, target_lon, float(row["latitude"]), float(row["longitude"]))
            
            # If photo is within the specified radius, display it
            if dist <= radius_km:
                print(row["filename"], f"{dist:.2f} km away")