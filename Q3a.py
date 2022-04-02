
def week(case):
    switcher = {
        "CSC2902": 'Career Professional Development',
        "CSC1006": 'Mathematics 2',
        "CSC1007": 'Operating Systems',
        "CSC1008": 'Data structures and Algorithms',
        "CSC1009": 'Object-Oriented Programming',
    }
    return switcher.get(case, "Unknown Module Code")


print("Please enter module code :")  # Print statement for module code
module = input()  # Storing input into module string
print(week(module))
