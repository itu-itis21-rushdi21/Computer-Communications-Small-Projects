date_data = []

max_time = float('-inf')
min_time = float('inf')

file_name = input("enter file name: ")
date = input("enter date: ")

with open(file_name, 'r') as file:
    lines = file.readlines()
    for line in lines:
        elements = line.strip().split(',')
        if elements[0] != "Mtr_Version" and elements[4] == "3" and elements[5] != "???":
            date_data.append(elements[10])
            element_11 = float(elements[11])
            element_12 = float(elements[12])
            if float(max_time) < element_12:
                max_time = elements[12]
            if float(min_time) > element_11:
                min_time = elements[11]    

with open(date +'_stats', 'w') as file:
    file.write("max_" + date + ": " + str(max_time) + "\n")
    file.write("min_" + date + ": " + str(min_time) + "\n")
    file.write(",".join(date_data))