"""This program will run the mtr command for each destination in the list and write the output to a file."""
"""it takes the time and date as input and then runs the mtr command for each destination in the list and writes the output to a file."""


import subprocess

# List of destinations to run

destination_list = ["www.google.com", "www.tum.de", "www.aalto.fi", "nus.edu.sg", "www.unimelb.edu.au" , "www.berkeley.edu", "www.mit.edu", "www.harvard.edu", "www.yale.edu", "www.utoronto.ca"]
repetitions_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# Create a list to store subprocess instances
processes = []
# Create a list to store the data instances 
data_list = []

input_date = input("enter date: ")
input_time = input("enter time: ")


# Start each command in a separate process
for destination in destination_list:  
    for i in range(len(repetitions_list)):
        process = subprocess.Popen("mtr -C -c" + str(repetitions_list[i]) + " "+  destination, shell=True, text=True, stdout=subprocess.PIPE)
        processes.append(process)

# Wait for all processes to finish
for process in processes:
    data_instance = ""
    # what does this do? it wait for the process to finish or for all the processes to finish? 
    #it causes them to wait for each other to finish? all of them then why in a for loop?
    process.wait()
    while True:
        line = process.stdout.readline()
        if not line:
            break
        data_instance += line
    data_list.append(data_instance)

# writes at one time for the list 
# makes writing to the data file noticably faster
with open(input_date + "_" +  input_time, "w") as f:
    for i in range(len(data_list)):
        f.write(data_list[i])    

print("All command prompts have finished.")