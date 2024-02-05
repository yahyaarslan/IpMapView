# IpMapView

IpMapView is a Python project that retrieves the public IP address of the user, geolocates it to get the real-world address and latitude/longitude, and then plots the location on a map using GeoPandas.

## Installation

1. Ensure you have the necessary Python libraries installed. You can install them using pip:

```bash
pip install geocoder shapely geopandas matplotlib
```

2. Run the `IpMapView.py` script:

```bash
python IpMapView.py
```

This will print the public IP address, the real-world address associated with the IP, and the latitude and longitude. If the geolocation is successful, it will also create a GeoDataFrame and plot a point at the location.

## Upcoming
+ Accounting for proxies, and plotting their connections. Useful for viewing countries the connections go through.
+ Traceback marking?