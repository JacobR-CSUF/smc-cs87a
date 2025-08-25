### Assignment 3

You will write a program that can convert a distance from either miles, kilometers, centimeters, or millimeters to an equivalent distance in meters.

The program must define the following functions:
- miles_to_meters
- kilometers_to_meters
- centimeters_to_meters
- millimeters_to_meters
- main()

**miles_to_meters** takes a single float as input, which represents the number of miles, and returns the equivalent number of meters according to the relationship of 1609.344 meters = 1 mile.

**kilometers_to_meters** takes a single float as input, which represents the number of kilometers, and returns the equivalent number of meters according to the relationship of 1000 meters = 1 kilometer.

**centimeters_to_meters** takes a single float as input, which represents the number of centimeters, and returns the equivalent number of meters according to the relationship of 1 meter = 100 centimeters.

**millimeters_to_meters** takes a single float as input, which represents the number of millimeters, and returns the equivalent number of meters according to the relationship of 1 meter = 1000 millimeters.

**main** takes no parameters and returns nothing. It asks the user for two input values. First, it asks for the number of units you will be converting. Then, it asks for the unit of distance itself. Once both inputs have been provided, it must print the equivalent distance in meters.
 **You may assume the first input will always be a valid number that can be converted to a float. You may assume the second input will always be one of the following strings: mi, km, cm, mm (you do not need to handle uppercase).**  

In summary, your program will do the following:

- Define miles_to_meters (this is done already in the starter file)
- Define kilometers_to_meters
- Define centimeters_to_meters
- Define millimeters_to_meters
- Define main()  
If it calls main(), it does so in the Python main conditional
It must do nothing else.
