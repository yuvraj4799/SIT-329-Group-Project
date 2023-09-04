# The Python library for SMBus can be used to communicate with I2C based devices.
import smbus
# It is for the time complexity of the program
import time
from datetime import datetime  # Import the datetime module
import csv  # Import the csv module

# Default address for the BH1750 sensor
BH1750_ADD = 0x23
RES_MODE = 0x20

# Instance
bus = smbus.SMBus(1)

# Function to read the measurement taken from the device (the reading comes in the form of 2-byte data)
def light_intensity(address, resolution):
    reading = bus.read_i2c_block_data(address, resolution)
    return conversion(reading)

# Function to convert the reading into a decimal number from two-byte data.
def conversion(input):
    return ((input[1] + (256 * input[0])) / 1.2)

def main():
    while True:
        # Reads the value.
        value = light_intensity(BH1750_ADD, RES_MODE)
        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Prints the value of light intensity along with the timestamp
        print(f"{timestamp} - Light Intensity: {value}")
        
        # Store the data with timestamps in a CSV file
        with open("light_intensity_data.csv", mode="a", newline="") as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([timestamp, value])
        
        time.sleep(1.0)

# Entry point of the program
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Computation Stopped!!")
