GPS Toll-based System Simulation Using Python
Overview
This project simulates a GPS toll-based system using Python. It generates GPS data, detects entry and exit from toll zones, calculates toll charges based on the time spent in each toll zone, and generates a detailed billing report.

Features
GPS Data Simulation: Generates random GPS data for vehicle locations and timestamps.
Toll Zone Detection: Identifies when a vehicle enters or exits predefined toll zones based on latitude and longitude.
Time-based Toll Calculation: Calculates toll charges based on the time spent in each toll zone and vehicle type.
Detailed Billing Report: Provides a comprehensive billing report including entry and exit times, time spent in toll zones, and total toll charges for different vehicle types.
Installation
To run this project, you need to have Python installed on your system. You can download Python from python.org.

Prerequisites
Python 3.x
Required Libraries
random: For generating random GPS data.
time: For handling timestamps and calculating time spent in toll zones.
Setup
Install Python:

Download and install Python from python.org.
Verify the installation by running python --version in your terminal.
Create a Project Directory:

Create a directory for your project and navigate to it in your terminal.
bash
Copy code
mkdir gps_toll_system
cd gps_toll_system
Create a Python Script:

Create a new Python file (e.g., gps_toll_system.py) in your project directory and paste the provided code into this file.
Usage
Run the Script:

Open a terminal and navigate to your project directory.
Run the Python script.
bash
Copy code
python gps_toll_system.py
Observe the Output:

The script will generate random GPS data for different vehicle types and calculate the toll charges based on the time spent in each toll zone.
It will print a detailed billing report for each vehicle type, including entry and exit times, time spent in toll zones, and total toll charges.
Code Explanation
Here's a point-by-point explanation of the code:

Import Libraries:

random: Used to generate random GPS data.
time: Used to handle timestamps and calculate time spent in toll zones.
python
Copy code
import random
import time
Generate GPS Data:

generate_gps_data(num_points): Generates a list of random GPS data points, each consisting of latitude, longitude, and timestamp.
python
Copy code
def generate_gps_data(num_points):
    gps_data = []
    for _ in range(num_points):
        lat = random.uniform(37.0, 38.0)  # Example latitude range
        lon = random.uniform(-122.0, -121.0)  # Example longitude range
        timestamp = time.time() + random.uniform(0, 3600)  # Random timestamp within an hour
        gps_data.append((lat, lon, timestamp))
    return gps_data
Define Toll Zones:

Defines toll zones with specific latitude and longitude ranges.
python
Copy code
toll_zones = [
    {'name': 'Zone 1', 'lat_range': (37.2, 37.4), 'lon_range': (-121.8, -121.6)},
    {'name': 'Zone 2', 'lat_range': (37.6, 37.8), 'lon_range': (-121.4, -121.2)}
]
Check Toll Zone Entry:

is_in_toll_zone(lat, lon, toll_zones): Checks if a given latitude and longitude fall within any defined toll zone.
python
Copy code
def is_in_toll_zone(lat, lon, toll_zones):
    for zone in toll_zones:
        if zone['lat_range'][0] <= lat <= zone['lat_range'][1] and zone['lon_range'][0] <= lon <= zone['lon_range'][1]:
            return zone['name']
    return None
Calculate Toll Charges:

calculate_toll(zone_name, time_spent, vehicle_type='car'): Calculates toll charges based on the time spent in a toll zone and the vehicle type.
python
Copy code
def calculate_toll(zone_name, time_spent, vehicle_type='car'):
    toll_rates = {
        'Zone 1': {'car': 0.10, 'truck': 0.20},  # Charge per second
        'Zone 2': {'car': 0.15, 'truck': 0.30}
    }
    return toll_rates[zone_name][vehicle_type] * time_spent
Generate Billing Information:

generate_billing_info(gps_data, vehicle_type): Tracks when a vehicle enters and exits a toll zone, calculates the time spent, and the corresponding toll charges. Stores detailed billing information including entry and exit times, time spent, and toll charges.
python
Copy code
def generate_billing_info(gps_data, vehicle_type):
    billing_info = []
    total_toll_charges = 0
    current_zone = None
    entry_time = None

    for lat, lon, timestamp in gps_data:
        zone = is_in_toll_zone(lat, lon, toll_zones)
        if zone != current_zone:
            if current_zone is not None:
                time_spent = timestamp - entry_time
                toll = calculate_toll(current_zone, time_spent, vehicle_type)
                total_toll_charges += toll
                billing_info.append({
                    'zone': current_zone,
                    'entry_time': entry_time,
                    'exit_time': timestamp,
                    'time_spent': time_spent,
                    'toll': toll
                })
            current_zone = zone
            entry_time = timestamp
    
    return billing_info, total_toll_charges
Simulate GPS Data and Calculate Tolls:

Generates GPS data for multiple vehicle types and calculates the toll charges based on the time spent in each toll zone.
python
Copy code
vehicle_types = ['car', 'truck']
all_billing_info = []

for vehicle_type in vehicle_types:
    gps_data = generate_gps_data(100)
    billing_info, total_toll_charges = generate_billing_info(gps_data, vehicle_type)
    all_billing_info.append({
        'vehicle_type': vehicle_type,
        'billing_info': billing_info,
        'total_toll_charges': total_toll_charges
    })
Output Detailed Billing Information:

Prints a detailed billing report for each vehicle type, including toll zones entered, entry and exit times, time spent, and total toll charges.
python
Copy code
for info in all_billing_info:
    print(f"Vehicle Type: {info['vehicle_type']}")
    print("Billing Details:")
    for entry in info['billing_info']:
        print(f"  Zone: {entry['zone']}, Entry Time: {time.ctime(entry['entry_time'])}, Exit Time: {time.ctime(entry['exit_time'])}, Time Spent: {entry['time_spent']:.2f} seconds, Toll: ${entry['toll']:.2f}")
    print(f"Total Toll Charges: ${info['total_toll_charges']:.2f}\n")




