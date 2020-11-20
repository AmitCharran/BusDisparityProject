import ast

file = open('info.txt', 'r')
lines = file.readlines()
file.close()

# To do:
    # if Published Line Ref contains 'SBS'
        # Save Vehicle Ref in an Array ***Do not save duplicates

for line in lines:
    dictionary = ast.literal_eval(line)
    print(dictionary['Published Line Ref'])