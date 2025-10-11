
distance = 0 
speed = 0.0
hour = 0
# Requirements:
# 1. Ask the user to enter the speed of the vehicle in mph
speed = float(input("enter the speed: "))
# 2. Ask the user to enter the number of hours traveled
time = int(float(input("how many hour did you drive?: ")))
# 3. Create a table header showing "Hour" and "Distance Traveled"
print("hour\tDistance traveled")
print('-'*25)
# 4. Use a for loop to calculate distance for each hour
for hour in range(1, time+1):
    distance = speed * hour 
    print(hour, "\t", distance)
# 5. Display the distance traveled for each hour in a table format
#
# Logic:
# - Use for hour in range(1, time + 1) to loop through each hour
# - Calculate distance = hour * speed for each hour
# - Display each row with hour number and distance traveled
#
# Formula: distance = time * speed
#
# Example:
# Enter the speed of the vehicle in mph: 60
# Enter the number of hours traveled: 3
# Hour	Distance Traveled
# ------------------------
# 1	 60.0
# 2	 120.0
# 3	 180.0
