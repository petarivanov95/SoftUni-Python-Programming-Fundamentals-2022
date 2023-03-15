import os

root_path = r'C:\Users\petar\Desktop\General\python\SoftUni-Python-Fundamentals-2022\31. Regular Expressions - Exercise'
problems = """
01_Capture the Numbers
02_Find Variable Names in Sentences
03_Find Occurrences of Word in Sentence
04_Extract Emails
05_Furniture
06_Extract the Links
"""

names = []
for line in problems.splitlines():
    new_str = ""
    for char in line:
        if char == " ":
            new_str += "_"
        else:
            new_str += char
            
    names.append(new_str.lower())

# print(names)
for name in names:
    # Create a file with the .py extension
    file_name = f"{name}.py"
    try:
        # Open the file in write mode, which creates the file if it doesn't exist
        with open(file_name, 'w') as f:
            # Write an empty string to the file, just to ensure it's created
            f.write("")
    except:
        pass
