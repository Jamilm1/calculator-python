import random

def generate_random_number():
    print("Random Number Generator")
    print("Select option:")
    print("1. Generate a random integer within a range")
    print("2. Generate a random floating-point number within a range")
    print("3. Generate a random number from a Gaussian distribution")
    
    while True:
        choice = input("Enter choice(1/2/3): ")

        if choice == '1':
            try:
                start = int(input("Enter the start of the range: "))
                end = int(input("Enter the end of the range: "))
                random_integer = random.randint(start, end)
                print(f"Random integer between {start} and {end}: {random_integer}")
            except ValueError:
                print("Invalid input. Please enter integer values.")
                
        elif choice == '2':
            try:
                start = float(input("Enter the start of the range: "))
                end = float(input("Enter the end of the range: "))
                random_float = random.uniform(start, end)
                print(f"Random float between {start} and {end}: {random_float}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                
        elif choice == '3':
            try:
                mean = float(input("Enter the mean: "))
                stddev = float(input("Enter the standard deviation: "))
                random_gaussian = random.gauss(mean, stddev)
                print(f"Random number from Gaussian distribution with mean {mean} and standard deviation {stddev}: {random_gaussian}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        
        next_generation = input("Do you want to generate another random number? (yes/no): ")
        if next_generation.lower() != 'yes':
            break

if __name__ == "__main__":
    generate_random_number()
