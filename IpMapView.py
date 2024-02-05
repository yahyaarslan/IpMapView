# Description: This script will display your public IP address on a map in Firefox.

# Install the rich library
from rich.traceback import install

install()


# Get the public IP address
import requests


import requests
import geocoder

def get_public_ip():
    response = requests.get("https://api.ipify.org")
    return response.text


# Get the real address and latitude/longitude
def get_real_address(ip):
    g = geocoder.ip(ip)
    if g.ok:
        return g.address, g.latlng
    else:
        return "Unable to retrieve address", None


# Get the public IP address
public_ip = get_public_ip()
print(public_ip)

# Get the real address and latitude/longitude
address, latlng = get_real_address(public_ip)
latitude = latlng[0]
longitude = latlng[1]
print(address)
if latlng:
    print(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    print("Unable to retrieve latitude and longitude")


# Create a GeoDataFrame with a point
from shapely.geometry import Point
import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.GeoDataFrame([{"geometry": Point(longitude, latitude)}])

# Load the world shapefile
# world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
world = gpd.read_file("110m_cultural/ne_110m_admin_0_countries.shp")

# Plot the world
world.plot()

# Plot the point
gdf.plot(ax=plt.gca(), color="red")

# Annotate the point
plt.annotate(
    text=address,
    xy=(longitude, latitude),
    xytext=(longitude + 10, latitude + 10),
    arrowprops=dict(arrowstyle="->", color="black"),
)

# Show the plot
plt.show()
