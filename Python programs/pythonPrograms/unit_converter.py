# Unit Converter (Length, Weight, Temperature, etc.)
def length_converter():
    meters = float(input("Enter length in meters: "))
    print(f"{meters} meters = {meters * 100} centimeters")
    print(f"{meters} meters = {meters * 39.37} inches")
    print(f"{meters} meters = {meters * 3.281} feet")

def weight_converter():
    kg = float(input("Enter weight in kilograms: "))
    print(f"{kg} kg = {kg * 1000} grams")
    print(f"{kg} kg = {kg * 2.205} pounds")

def temp_converter():
    c = float(input("Enter temperature in Celsius: "))
    print(f"{c}°C = {(c * 9/5) + 32}°F")
    print(f"{c}°C = {c + 273.15}K")

def main():
    while True:
        print("1. Length 2. Weight 3. Temperature 4. Exit")
        choice = input("Choice: ")
        if choice == '1':
            length_converter()
        elif choice == '2':
            weight_converter()
        elif choice == '3':
            temp_converter()
        elif choice == '4':
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()
