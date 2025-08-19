# Photo Library EXIF Metadata Article

A Python project for extracting, indexing, and searching photo metadata using EXIF data. This project demonstrates how to work with photo metadata including GPS coordinates, timestamps, camera information, and more.

If these scripts were useful to you, consider donating to support the Developer Service Blog: https://buy.stripe.com/bIYdTrggi5lZamkdQW

## Features

- **EXIF Metadata Extraction**: Extract comprehensive metadata from photos including:

  - GPS coordinates (latitude, longitude, altitude)
  - Timestamp information
  - Camera model and settings
  - File information

- **Photo Indexing**: Create searchable CSV indexes of your photo library
- **Geographic Search**: Find photos by location using:
  - Exact coordinate matching
  - Radius-based searching with the Haversine formula
- **Multiple Image Formats**: Support for JPG, JPEG, and TIFF files

## Files

- **`main.py`**: Main script for extracting metadata and building photo indexes
- **`simple_search.py`**: Simple exact-coordinate photo search
- **`advanced_search.py`**: Advanced radius-based photo search using the Haversine formula
- **`requirements.txt`**: Python dependencies
- **`photo_index.csv`**: Generated photo metadata index (created after running main.py)

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd Photo-Library-EXIF-Metadata-Article
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Build Photo Index

First, create an index of your photos:

```bash
python main.py
```

This will:

- Scan the current directory for image files
- Extract EXIF metadata from each image
- Create a `photo_index.csv` file with all the metadata

### 2. Simple Search

Find photos taken at exact coordinates:

```bash
python simple_search.py
```

This searches for photos taken at exactly the specified London coordinates (51.5074°N, -0.1278°W).

### 3. Advanced Search

Find photos within a radius of a location:

```bash
python advanced_search.py
```

This uses the Haversine formula to find photos within 10km of the target location.

## Configuration

### Target Location

Edit the coordinates in the search scripts to find photos in different locations:

```python
# Change these coordinates to your desired location
target_lat, target_lon = 51.5074, -0.1278  # London, UK
```

### Search Radius

In `advanced_search.py`, modify the radius:

```python
radius_km = 10  # Change to your desired search radius
```

### Photo Directory

In `main.py`, change the directory to scan:

```python
build_index(".")  # Current directory
# or
build_index("path/to/your/photos")  # Custom directory
```

## Mathematical Background

### Haversine Formula

The advanced search uses the Haversine formula to calculate great-circle distances between two points on Earth's surface:

```
d = R × c
```

Where:

- `R` = Earth's radius (6,371 km)
- `c` = Angular distance in radians
- `d` = Distance in kilometers

This formula accounts for Earth's curvature and provides accurate distance calculations for geographic searches.

## Supported Image Formats

- **JPEG** (.jpg, .jpeg)
- **TIFF** (.tiff)

## Dependencies

- **exif**: Python library for reading EXIF metadata from images
- **csv**: Built-in Python module for CSV file handling
- **os**: Built-in Python module for file system operations
- **pathlib**: Built-in Python module for path handling
- **math**: Built-in Python module for mathematical operations

## Example Output

### Photo Index (photo_index.csv)

```csv
filename,timestamp,latitude,longitude,altitude,camera
england-london-bridge.jpg,2023:06:15 14:30:22,51.5074,-0.1278,35.0,Canon EOS R5
```

### Search Results

```
england-london-bridge.jpg 0.00 km away
```

## Troubleshooting

### Common Issues

1. **No GPS data found**: Some images may not have GPS coordinates embedded
2. **Permission errors**: Ensure you have read access to the image files
3. **Missing dependencies**: Run `pip install -r requirements.txt`

### Debug Mode

Add print statements to see what metadata is being extracted:

```python
metadata = extract_metadata(image_path)
print(f"Extracted: {metadata}")
```

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Uses the `exif` library for EXIF data extraction
- Implements the Haversine formula for geographic distance calculations
- Designed for educational purposes and practical photo library management
