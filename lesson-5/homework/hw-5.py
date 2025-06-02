
##Task1


def convert_cel_to_far(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

def convert_far_to_cel(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def main():
    fahrenheit = float(input("Enter a temperature in degrees F: "))
    celsius = convert_far_to_cel(fahrenheit)
    print(f"{fahrenheit} degrees F = {round(celsius, 2)} degrees C\n")

    celsius = float(input("Enter a temperature in degrees C: "))
    fahrenheit = convert_cel_to_far(celsius)
    print(f"{celsius} degrees C = {round(fahrenheit, 2)} degrees F")

if __name__ == "__main__":
    main()


##Task2

def convert_cel_to_far(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

def convert_far_to_cel(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def main():
    fahrenheit = float(input("Enter a temperature in degrees F: "))
    celsius = convert_far_to_cel(fahrenheit)
    print(f"{fahrenheit:.2f} degrees F = {celsius:.2f} degrees C\n")

    celsius = float(input("Enter a temperature in degrees C: "))
    fahrenheit = convert_cel_to_far(celsius)
    print(f"{celsius:.2f} degrees C = {fahrenheit:.2f} degrees F")

if __name__ == "__main__":
    main()


##Task3

def main():
    try:
        number = int(input("12: "))
        if number <= 0:
            print("You must enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")
        return

    for i in range(1, number + 1):
        if number % i == 0:
            print(f"{i} is a factor of {number}")

if __name__ == "__main__":
    main()


##Task4

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(data):
    """Extracts student enrollments and tuition fees from university data."""
    enrollments = [univ[1] for univ in data]
    tuitions = [univ[2] for univ in data]
    return enrollments, tuitions

def mean(numbers):
    """Returns the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

def median(numbers):
    """Returns the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2

    if n % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]

enrollments, tuitions = enrollment_stats(universities)

total_students = sum(enrollments)
total_tuition = sum(tuitions)

mean_students = mean(enrollments)
median_students = median(enrollments)

mean_tuition = mean(tuitions)
median_tuition = median(tuitions)

print("*" * 30)
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print()
print(f"Student mean: {mean_students:,.2f}")
print(f"Student median: {int(median_students):,}")
print()
print(f"Tuition mean: $ {mean_tuition:,.2f}")
print(f"Tuition median: $ {int(median_tuition):,}")
print("*" * 30)


##Task5

def is_prime(n):
    """Returns True if n is a prime number, otherwise False."""
    if n <= 1:
        return False 
    if n == 2:
        return True  
    if n % 2 == 0:
        return False  

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
print(is_prime(1)) 
print(is_prime(2))
print(is_prime(17)) 
print(is_prime(18)) 
