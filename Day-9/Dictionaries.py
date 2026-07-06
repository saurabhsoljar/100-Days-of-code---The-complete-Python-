programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing somthing over and over again",

}

# print(programming_dictionary["Bug"])
# print(programming_dictionary["Function"])
# print(programming_dictionary["Loop"])

programming_dictionary["Bug"]="A moth in your Computer."
print(programming_dictionary)

# Loop through a dictionary

for key in programming_dictionary:
    # print(thing)
    print(key)
    print(programming_dictionary[key])