import ast

file = open('info.txt', 'r')
lines = file.readlines()
file.close()

# To do:
    # if Published Line Ref contains 'SBS'
        # Save Vehicle Ref in an Array ***Do not save duplicates
Vehicles =[]
for line in lines:
    dictionary = ast.literal_eval(line)
    a = dictionary['Published Line Ref'][-3:]
    b = dictionary['Vehicle Ref']
    if(a=="SBS"):
        if b in Vehicles:
            continue
        else:
            Vehicles.append(b)


print(Vehicles)
    # print(dictionary['Published Line Ref'])