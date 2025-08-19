import csv

# Define the target location (London, UK coordinates)
target_lat, target_lon = 51.5074, -0.1278

# Open and read the photo index CSV file that contains photo metadata
with open("photo_index.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    
    # Process each row (photo) in the CSV file
    for row in reader:
        # Check if both latitude and longitude data exist for this photo
        if row["latitude"] and row["longitude"]:
            # Perform exact coordinate match - check if photo was taken at exactly the target location
            if float(row["latitude"]) == target_lat and float(row["longitude"]) == target_lon:
                print(row["filename"])