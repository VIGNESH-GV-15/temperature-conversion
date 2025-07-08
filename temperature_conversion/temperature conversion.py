def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    unit = unit.lower()
    
    if unit == "celsius" or unit == "c":
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        print(f"\n{value:.2f}°C is equal to:")
        print(f"{f:.2f}°F")
        print(f"{k:.2f} K")
    
    elif unit == "fahrenheit" or unit == "f":
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        print(f"\n{value:.2f}°F is equal to:")
        print(f"{c:.2f}°C")
        print(f"{k:.2f} K")
    
    elif unit == "kelvin" or unit == "k":
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        print(f"\n{value:.2f} K is equal to:")
        print(f"{c:.2f}°C")
        print(f"{f:.2f}°F")
    
    else:
        print("Invalid temperature unit. Please enter Celsius, Fahrenheit, or Kelvin.")

def main():
    print("Temperature Converter")
    try:
        value = float(input("Enter the temperature value: "))
        unit = input("Enter the unit (Celsius, Fahrenheit, Kelvin): ")
        convert_temperature(value, unit)
    except ValueError:
        print("Invalid input. Please enter a numeric temperature value.")

if __name__ == "__main__":
    main()