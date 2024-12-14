### Functions
def greet():
    print("Hello")
    print("Howdy")


greet()

### Arguments vs Params
#Params
def greet_with_name(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

#Args
greet_with_name("Kristine", "Wildheart")

### Types of functions
# 1- Perform a task
def greet_with_name_2(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


greet_with_name_2("Kristine", "Wildheart")

# 2- Return a value
def get_greeting(name):
    return f"Hello, {name}!"

message = get_greeting("Kristine")
print(message)
file=open("name.txt", "w")
file.write(message)
file.close()

def increment(number, by):
    return number + by


print(increment(number=2, by=3))

### Default args
def increment_1(number, by=1):
    return number + by


print(increment_1(number=2))

# ANorther example (*args)
# def multiply(*numbers):
#     print(numbers)
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(1,2,3,4,5))

### ***args
def save_user(**user):
    print(user['id'])
    print(user['name'])


save_user(id=1,name="Kristine", last_name="Wildheart")

### Exercise(fizz, buzz)
# Function returns different results depending on input
# If input %3==0 return fizz
# If input %5==0 return Buzz
# If input %3 ==0 and %5==0 fizzbuzz
# else return input

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    return number

print(fizz_buzz(7))