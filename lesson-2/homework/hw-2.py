##Number Data Type Questions
##num1

number = float(input("12.34567 : "))

rounded_number = round(number, 2)

print("Rounded number (2 decimal places):", rounded_number)

##num2 


num1 = float(input("12: "))
num2 = float(input("45: "))
num3 = float(input("7: "))

largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

print("The largest number is:", largest)
print("The smallest number is:", smallest)

##num3


kilometers = float(input("3.5: "))

meters = kilometers * 1000
centimeters = kilometers * 100000

print(f"{kilometers} kilometers is equal to:")
print(f"{meters} meters")
print(f"{centimeters} centimeters")


#num4

num1 = int(input("13: "))
num2 = int(input("3: "))

if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    quotient = num1 // num2
    remainder = num1 % num2

    print("Quotient:", quotient)
    print("Remainder:", remainder)

##num5


celsius = float(input("23: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit}°F")

##num6


number = int(input("345: "))

last_digit = abs(number) % 10  

print(f"The last digit of {number} is {last_digit}")

##num7


number = int(input("44: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

##String Questions
##num1

from datetime import datetime

name = input("Jama: ")
year_of_birth = int(input("2008: "))

current_year = datetime.now().year

age = current_year - year_of_birth

print(f"Hello {name}, you are {age} years old.")

##num2


txt = 'LMaasleitbtui'.lower()  

car_names = [
    'bmw', 'audi', 'ford', 'toyota', 'tesla', 'jeep', 'honda',
    'kia', 'hyundai', 'volvo', 'mazda', 'mini', 'fiat', 'lexus',
    'nissan', 'subaru', 'jaguar', 'buick'
]

found_cars = [car for car in car_names if car in txt]

if found_cars:
    print("nissan:", found_cars)
else:
    print("No recognizable car names found.")

##num3


user_input = input("Wassup Jama: ")

print("Length of the string:", len(user_input))

print("Uppercase:", user_input.upper())

print("Lowercase:", user_input.lower())


#num4


user_input = input("Madam: ")

cleaned_input = user_input.replace(" ", "").lower()

if cleaned_input == cleaned_input[::-1]:
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")

##num5

user_input = input("Wassup Jama: ")

vowels = 0
consonants = 0

vowel_set = "aeiou"

for char in user_input.lower():
    if char.isalpha():  
        if char in vowel_set:
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)

##num6


main_string = input("Wassup Jama: ")
search_string = input("Jama: ")

if search_string in main_string:
    print(f"Yes, '{main_string}' contains '{search_string}'.")
else:
    print(f"No, '{main_string}' does not contain '{search_string}'.")

##num7


sentence = input("I love apples: ")
word_to_replace = input("apples ")
replacement_word = input("oranges: ")

new_sentence = sentence.replace(word_to_replace, replacement_word)

print("Updated sentence:", new_sentence)

##num8


user_input = input("Jama: ")

if len(user_input) > 0:
    first_char = user_input[0]
    last_char = user_input[-1]
    print("J:", first_char)
    print("a:", last_char)
else:
    print("You entered an empty string.")


##num9


user_input = input("Jama: ")

reversed_string = user_input[::-1]

print("amaJ:", reversed_string)

##num10



sentence = input("I came to learn Python: ")

words = sentence.split()

word_count = len(words)

print("5:", word_count)

##num11


user_input = input("Jama33: ")

contains_digit = any(char.isdigit() for char in user_input)

if contains_digit:
    print("The string contains digits.")
else:
    print("The string does not contain any digits.")

##num12


words_input = input("Jama Asco Doni: ")

words_list = words_input.split()

separator = input("-: ")

joined_string = separator.join(words_list)

print("Joined string:", joined_string)

##num13


string1 = input("Jama: ")
string2 = input("jama: ")

if string1 == string2:
    print("The strings are equal.")
else:
    print("The strings are not equal.")

#num14


sentence = input("World Health Organization: ")

words = sentence.split()

acronym = ''.join(word[0].upper() for word in words if word)

print("WHO:", acronym)

##num15


user_string = input("Jama Nigga: ")

char_to_remove = input("a: ")

result_string = user_string.replace(char_to_remove, '')

print("Jm Nigg:", result_string)

##num16


user_input = input("Jama Nigga: ")

vowels = "aeiouAEIOU"

replaced_string = ''.join('*' if char in vowels else char for char in user_input)

print("J*m* N*gg*:", replaced_string)


##num17


sentence = input("Python is fun!: ")

start_word = input("Python: ")
end_word = input("fun!: ")

if sentence.startswith(start_word) and sentence.endswith(end_word):
    print("Yes, the sentence starts with and ends with the specified words.")
else:
    print("No, the sentence does not match the given start or end.")

##num18


username = input("Jama33: ")
password = input("Nigga33: ")

if username and password:
    print("Login details accepted.")
else:
    print("Error: Username and password cannot be empty.")

##Boolean Data Type Questions
##num1


num1 = float(input("33: "))
num2 = float(input("33: "))

if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

##num2


number = int(input("6: "))

if number > 0 and number % 2 == 0:
    print("The number is positive and even.")
else:
    print("The number is not both positive and even.")

##num3


num1 = float(input("3: "))
num2 = float(input("10: "))
num3 = float(input("18: "))

if num1 != num2 and num1 != num3 and num2 != num3:
    print("All numbers are different.")
else:
    print("Some numbers are the same.")

##num4


string1 = input("wassup: ")
string2 = input("jama: ")

if len(string1) == len(string2):
    print("Both strings have the same length.")
else:
    print("The strings have different lengths.")

##num5


number = int(input("15: "))

if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")

##num6


num1 = float(input("25.4: "))
num2 = float(input("28: "))

total = num1 + num2

if total > 50.8:
    print("The sum is greater than 50.8.")
else:
    print("The sum is not greater than 50.8.")
