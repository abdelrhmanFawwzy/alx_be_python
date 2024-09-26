FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    result = (fahrenheit - 32) / CELSIUS_TO_FAHRENHEIT_FACTOR
    return result


def convert_to_fahrenheit(celsius):
    result = (celsius  * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return result


def main():
    temp = float(input("Enter the temperature to convert: "))
    choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
    if choice == "c":
        global f
        f = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {f}°F")
    elif choice == "f":
        global c
        c = convert_to_celsius(temp)
        print(f"{temp}°F is {c}°C")
    else:
        print("invalid input.")
        
        
if __name__ == "__main__":
    main()   