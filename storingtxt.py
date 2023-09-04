# The Python library for SMBus can be used to communicate with I2C based devices.
import smbus
# It is for the time complexity of the program
import time

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
        # Prints the value of light intensity
        print("Light Intensity: " + str(value))
        
        # Store the data in a file
        with open("light_intensity_data.txt", "a") as file:
            file.write(str(value) + "\n")
        
        time.sleep(1.0)

# Entry point of the program
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Computation Stopped!!")
