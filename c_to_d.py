#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: November 2019
# This is a program which converts degrees from celcius to farenheit.


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


degrees = 0


def main():
    # This is what runs the program.
    global degrees

    print("This program converts a temperature from degrees Celcius"
          " to degrees Fahrenheit.")

    while True:
        degrees_as_string = input(color.YELLOW + color.BOLD +
                                  'Input the temperature in degrees Celcius:' +
                                  color.END)
        try:
            degrees = int(degrees_as_string)
            calculations()
            break

        except Exception:
            print('')
            print(color.PURPLE + color.UNDERLINE + 'That is not a valid'
                  ' number...' + color.END)
            print("")
            print("")


def calculations():
    global degrees

    fahrenheit = (9/5)*degrees+32
    print("{0} degrees fahrenheit.".format(fahrenheit))


if __name__ == "__main__":
    main()
