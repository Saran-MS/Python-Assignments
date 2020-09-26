import re

flight_details="Good Evening, Welcome to British Airways. Your flight number is ba8004. Flight departure time is 16:45"

name = re.search("British Airways",flight_details)
if name:
    print("British Airways")
else :
    print("No Output")
    
time = re.findall("16:45",flight_details)

if time:
    print("16:45")
else:
    print("No output")
    
details = re.search("^Good",flight_details)

if details:
    print("Good")
else:
    print("No output")
    
find = re.search("F[a-zA-Z]{5}",flight_details)

if find:
    print(find.group())
else :
    print("No output")
    
replace = re.search("ba\d{4}",flight_details)

if replace:
    print(re.sub('ba(\d{4})',r'ba\1'.upper(),flight_details))
