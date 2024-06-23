# #!/usr/bin/python3
# print("Content-type: text/html")
# print("\n")

# import geocoder

# def get_current_location():
#     # Get current coordinates
#     current_location = geocoder.ip('me')
    
#     if current_location.ok and current_location.latlng:
#         latitude, longitude = current_location.latlng
#     else:
#         raise Exception("Unable to get current location from IP address.")

#     # Get current location using reverse geocoding
#     location_info = geocoder.osm([latitude, longitude], method='reverse')
    
#     if location_info.ok:
#         address = location_info.address
#     else:
#         address = "Address not found."

#     return latitude, longitude, address

# # Example usage:
# try:
#     latitude, longitude, location = get_current_location()
#     print("Latitude:", latitude)
#     print("Longitude:", longitude)
#     print("Location:", location)
# except Exception as e:
#     print("Error:", e)

#!/usr/bin/env python3

#!/usr/bin/env python3
import cgi
import cgitb
import json
from geopy.geocoders import Nominatim

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: application/json\n")

try:
    # Parse the query parameters
    form = cgi.FieldStorage()
    location_name = form.getvalue("location")

    if not location_name:
        raise ValueError("No location provided")

    # Function to get coordinates
    def get_coordinates(location_name):
        geolocator = Nominatim(user_agent="my_geocoder")
        location = geolocator.geocode(location_name)
        if location:
            return {"latitude": location.latitude, "longitude": location.longitude, "address": location.address}
        else:
            return {"error": "Location not found"}

    # Get coordinates for the provided location
    coordinates = get_coordinates(location_name)

    # Output the result as JSON
    print(json.dumps(coordinates))

except Exception as e:
    # Output error as JSON
    print(json.dumps({"error": str(e)}))
