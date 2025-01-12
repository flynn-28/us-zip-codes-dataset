import csv # import csv library for parsing data

data = {} # initialize variable to store data
with open('/kaggle/input/united-states-zipcodes/zipcodes.csv', mode='r') as file: # open the data 
  reader = csv.DictReader(file) # define csv reader
  for row in reader: # read each row of data
    data[row['zip']] = row # store row into data

search = "14779" # define zipcode to search, stored as strings
    
result = data.get(search, "zip not found") # search the data for a zipcode, return error if not found
    
if result != "zip not found": # if there wasnt an error
  print(f"State: {result['state']}") # print state of zipcode
  print(f"County: {result['county']}") # print county of zipcode
  print(f"City: {result['city']}") # print city of zipcode
  print(f"Timezone: {result['timezone']}") # print timezone of zipcode
  print(f"Coordinates: {result['coordinates']}") # print coordinates of zipcode
else:
  print(result) # print error message
