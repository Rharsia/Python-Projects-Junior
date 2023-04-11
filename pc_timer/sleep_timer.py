import time
import os

print("This is a timer to turn off (sleep) the PC")
print()

# get the number of minutes from the user
minutes = float(input("Enter the number of minutes: "))

# convert to seconds
seconds = round(minutes * 60)

# display the message
print(f"The computer will sleep in {minutes} minutes.")

# loop through the countdown timer
for i in range(seconds, 0, -1):
    # calculate the minutes and seconds remaining
    mins, secs = divmod(i, 60)

    # display the remaining time
    print(f"{mins:02d}:{secs:02d}", end="\r")

    # wait for one second
    time.sleep(1)

print("SHUTDOWN")

os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")