import time
import csv
import os
import sys
import select
from datetime import datetime

# Function to print the ASCII art
def print_ascii_art():
    ascii_art = '''
 ||||||||||||||||||||||||||||||||||||||||||||||
 ||||||||||||||||||||||||||||||||||||||||||||||
 ||||||||||||||||||||||||||||||||||||||||||||||
 ||||||||||||||||||||||||||||||||||||||||||||||
                    ___           ___                         ___
     _____         /\__\         /\  \                       /\  \\
    /::\  \       /:/ _/_       /::\  \         ___          \:\  \\
   /:/\:\  \     /:/ /\__\     /:/\:\  \       /\__\          \:\  \\
  /:/  \:\__\   /:/ /:/ _/_   /:/ /::\  \     /:/  /      ___ /::\  \\
 /:/__/ \:|__| /:/_/:/ /\__\ /:/_/:/\:\__\   /:/__/      /\  /:/\:\__\\
 \:\  \ /:/  / \:\/:/ /:/  / \:\/:/  \/__/  /::\  \      \:\/:/  \/__/
  \:\  /:/  /   \::/_/:/  /   \::/__/      /:/\:\  \      \::/__/
   \:\/:/  /     \:\/:/  /     \:\  \      \/__\:\  \      \:\  \\
    \::/  /       \::/  /       \:\__\          \:\__\      \:\__\\
     \/__/         \/__/         \/__/           \/__/       \/__/
\n
 ||BORN: 18/02/2024||
 ||VERSION 1.0||
\n
 ||DYNAMIC.ENTITY.ASSESSING.TRANsITING.HUMANS||
 ||||||||||||||||||||||||||||||||||||||||||||||
 ||||||||||||||||||||||||||||||||||||||||||||||
 ||||||||||||||||||||||||||||||||||||||||||||||'''

    print(ascii_art)

# Function to initialize the counter
def initialize_counter():
    deaths = 0
    if os.path.isfile('deaths.csv'):
        with open('deaths.csv', 'r') as file:
            deaths = float(next(csv.reader(file))[0])
        deaths += (time.time() - os.path.getmtime('deaths.csv')) * 2
    else:
        # Calculate the number of seconds between 6 PM on 18/02/2024 and the current time
        start_time = datetime(2024, 2, 18, 18, 0, 0)
        current_time = datetime.now()
        seconds_since_start = (current_time - start_time).total_seconds()
        deaths = seconds_since_start * 2

    return deaths

# Function to save the last number in the counter to a CSV file
def save_counter_to_csv(deaths):
    with open('deaths.csv', 'w', newline='') as file:
        csv.writer(file).writerow([deaths])

# Function to start counting deaths
def start_counting_deaths():
    deaths = initialize_counter()
    print_ascii_art()
    while True:
        deaths += 2
        print(f" DEATHS : {deaths:.2f}", end="\r")
        time.sleep(1)
        if select.select([sys.stdin,],[],[],0.0)[0]:
            user_input = input()
            if user_input == "":
                save_counter_to_csv(deaths)
                break

# Start counting deaths
start_counting_deaths()
