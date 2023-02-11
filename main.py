zones = []
bssid = []
threashold = 5
# Load training data from csv file
with open('training_data.csv') as data_file:
    data = data_file.readlines()
    zone_1 = []  # zone 1 data
    zone_2 = []  # zone 2 data
    zone_3 = []  # zone 3 data
    zone_4 = []  # zone 4 data
    # Load data from row 1 because it's the header
    # and less than 8, the size of data because its noise
    for i in range(1, len(data) - 8):
        # split the riid into zones
        csv_split = data[i].split(',')
        bssid.append(csv_split[0].replace('\n', '').strip())
        zone_1.append(csv_split[1].replace('\n', '').strip())
        zone_2.append(csv_split[2].replace('\n', '').strip())
        zone_3.append(csv_split[3].replace('\n', '').strip())
        zone_4.append(csv_split[4].replace('\n', '').strip())
    # append zones into one
    zones.append(zone_1)
    zones.append(zone_2)
    zones.append(zone_3)
    zones.append(zone_4)
# Get the path of new dataset
new_dataset_location = input('Please enter the path of dataset : ')
# Load data from the new dataset
with open(new_dataset_location) as new_data:
    data = new_data.readlines()
    new_zone = {}
    # Don't load data from header
    for i in range(1, len(data)):

        csv_split = data[i].split(',')
        new_zone[csv_split[0].replace('\n', '').strip()] = csv_split[1].replace('\n', '').strip()
# Percent match of each zone
percent_match = []
for zone in zones:
    # How many matches in the current zone
    match_with_zone = 0
    for new_value in new_zone.keys():
        for zone_value, bssid_value in zip(zone, bssid):
            upper_bound = abs(int(zone_value)) + threashold
            lower_bound = abs(int(zone_value)) - threashold
            new_value_to_int = abs(int(new_zone[new_value]))
            in_range = lower_bound <= new_value_to_int <= upper_bound
            if in_range and new_value == bssid_value:
                # If there was a match, increment the value
                match_with_zone += 1
                break
    # Append percent match of the zone
    percent_match.append((match_with_zone / len(new_zone)) * 100)
max_match = -99999
# Find max match
for match in percent_match:
    if max_match < match:
        max_match = match
# Get zone from, where the match is coming from
print(percent_match)
print('The data is coming from zone : ' + str(percent_match.index(max_match) + 1))
