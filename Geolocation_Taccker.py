import requests
import folium

# Get data
data = requests.get("http://ip-api.com/json/").json()

# Print location
print("City:", data["city"])
print("Country:", data["country"])

# Create map
map = folium.Map(location=[data["lat"], data["lon"]], zoom_start=10)

# Add marker
folium.Marker([data["lat"], data["lon"]]).add_to(map)

# Save map
map.save("location.html")

print("Map saved! Open location.html")

