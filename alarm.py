# Patrick Mogianesi
# Updated /Augest 24 2016/

# This stack  overflow helped http://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list-with-python

# Import libraries
import time
import webbrowser
import random
import os

# Check if the user has the YT.txt file in the same directory as this script
if not os.path.isfile("YT.txt"):
    print("ERROR: YT.txt file not present. Creating file...")
    # Create the file and write a default URL
    with open("YT.txt", 'w') as file:
        file.write("https://youtu.be/BZg8BhBWyo8")

# Prompt the user to set the wake-up time
print("What time do you want to wake up?")
print("Use this format:\nExample: 06:30")
alarm_time = input("> ")

# Get the current time
current_time = time.strftime("%H:%M")

# Read the YouTube links from the file
with open("YT.txt") as f:
    # Read URLs and strip any extra whitespace
    urls = [line.strip() for line in f]

# Wait until the current time matches the alarm time
while current_time != alarm_time:
    print(f"The time is {current_time}")
    time.sleep(1)
    # Update the current time
    current_time = time.strftime("%H:%M")

# When the time matches the alarm time, activate the alarm
print("Time to Wake up!")
# Choose a random YouTube link
random_video = random.choice(urls)
# Open the chosen YouTube link in the web browser
webbrowser.open(random_video)

