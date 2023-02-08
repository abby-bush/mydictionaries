"""
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

"""

# Load the infile
import json

infile = open("eq_data.json", "r")
earthquakes = json.load(infile)


earthquakes["features"][0]["properties"]["type"]

# Print the number of earthquakes
print(len(earthquakes["features"]))


# Create and print 'eq_dict'
eq_dict = {}
x = 0

for earthquake in earthquakes["features"]:
    if earthquakes["features"][x]["properties"]["mag"] > 6:
        location = earthquakes["features"][x]["properties"]["place"]
        magnitude = earthquakes["features"][x]["properties"]["mag"]
        longitude = earthquakes["features"][x]["geometry"]["coordinates"][0]
        latitude = earthquakes["features"][x]["geometry"]["coordinates"][1]

        eq_dict[location] = [magnitude, longitude, latitude]

    x += 1

print(eq_dict)


# Print Earthquake Report
for earthquake in eq_dict:
    print(f"Location: {earthquake}")
    print(f"Magnitude: {eq_dict[earthquake][0]}")
    print(f"Longitude: {eq_dict[earthquake][1]}")
    print(f"Latitude: {eq_dict[earthquake][2]}")
    print()
    print()