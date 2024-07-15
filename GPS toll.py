import random
import time

# Generate GPS data
def generate_gps_data(num_points):
    gps_data = []
    for _ in range(num_points):
        lat = random.uniform(37.0, 38.0)  # Example latitude range
        lon = random.uniform(-122.0, -121.0)  # Example longitude range
        gps_data.append((lat, lon))
    return gps_data

# Define toll zones
toll_zones = [
    {'name': 'Zone 1', 'lat_range': (37.2, 37.4), 'lon_range': (-121.8, -121.6)},
    {'name': 'Zone 2', 'lat_range': (37.6, 37.8), 'lon_range': (-121.4, -121.2)}
]

def is_in_toll_zone(lat, lon, toll_zones):
    for zone in toll_zones:
        if zone['lat_range'][0] <= lat <= zone['lat_range'][1] and zone['lon_range'][0] <= lon <= zone['lon_range'][1]:
            return zone['name']
    return None

# Calculate toll charges
def calculate_toll(zone_name, vehicle_type='car'):
    toll_rates = {
        'Zone 1': {'car': 2.50, 'truck': 5.00},
        'Zone 2': {'car': 3.00, 'truck': 6.00}
    }
    return toll_rates[zone_name][vehicle_type]

# Simulate different vehicle types
vehicle_types = ['car', 'truck']

# Generate detailed billing information
def generate_billing_info(gps_data, vehicle_type):
    billing_info = []
    total_toll_charges = 0
    for lat, lon in gps_data:
        zone = is_in_toll_zone(lat, lon, toll_zones)
        if zone:
            toll = calculate_toll(zone, vehicle_type)
            total_toll_charges += toll
            billing_info.append({'latitude': lat, 'longitude': lon, 'zone': zone, 'toll': toll})
    return billing_info, total_toll_charges

# Simulate GPS data and calculate tolls for multiple vehicles
all_billing_info = []
for vehicle_type in vehicle_types:
    gps_data = generate_gps_data(100)
    billing_info, total_toll_charges = generate_billing_info(gps_data, vehicle_type)
    all_billing_info.append({'vehicle_type': vehicle_type, 'billing_info': billing_info, 'total_toll_charges': total_toll_charges})

# Output detailed billing information
for info in all_billing_info:
    print(f"Vehicle Type: {info['vehicle_type']}")
    print("Billing Details:")
    for entry in info['billing_info']:
        print(f"  Latitude: {entry['latitude']:.4f}, Longitude: {entry['longitude']:.4f}, Zone: {entry['zone']}, Toll: ${entry['toll']:.2f}")
    print(f"Total Toll Charges: ${info['total_toll_charges']:.2f}\n")
