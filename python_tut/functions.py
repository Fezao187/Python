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