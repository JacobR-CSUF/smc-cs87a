# CS 87A Lu -- Module 4 Assignment
# STUDENT NAME: Jacob Rodas
def miles_to_meters(miles):
  meters = miles * 1609.344
  return meters

def kilometers_to_meters(kilometers):
  meters = kilometers * 1000
  return meters

def centimeters_to_meters(centimeters):
  meters = centimeters / 100
  return meters

def millimeters_to_meters(millimeters):
  meters = millimeters / 1000
  return meters

#prompt user for distance and unit type (mi/km/cm/mm) to convert to meters.
def main():
  num_units = float(input("How many units are you converting: "))
  unit_type = input("Which units are you converting from (mi/km/cm/mm): ")

#determine unit type, then use appropriate function to calculate into meters.
  if unit_type == "mi":
    print(miles_to_meters(num_units), "meters")
  elif unit_type == "km":
    print(kilometers_to_meters(num_units), "meters")
  elif unit_type == "cm":
    print(centimeters_to_meters(num_units), "meters")
  elif unit_type == "mm":
    print(millimeters_to_meters(num_units), "meters")
  else:
    print("Invalid unit type.")

if __name__ == "__main__":
main()
