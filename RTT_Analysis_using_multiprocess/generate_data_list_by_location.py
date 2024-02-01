destination_list = ["www.google.com", "www.tum.de", "www.aalto.fi", "nus.edu.sg", "www.unimelb.edu.au", "www.berkeley.edu", "www.mit.edu", "www.harvard.edu", "www.yale.edu", "www.utoronto.ca"]

destination_data = {destination: {'max_time': float('-inf'), 'min_time': float('inf'), 'values': []} for destination in destination_list}

file_name = input("enter file name: ")

with open(file_name, 'r') as file:
    lines = file.readlines()
    for line in lines:
        elements = line.strip().split(',')
        if elements[0] != "Mtr_Version" and elements[4] == "3" and elements[5] != "???":
            destination = elements[3]
            destination_stats = destination_data.get(destination)
            if destination_stats:
                destination_stats['values'].append(elements[10])
                max_time = float(elements[12])
                min_time = float(elements[11])
                destination_stats['max_time'] = max(destination_stats['max_time'], max_time)
                destination_stats['min_time'] = min(destination_stats['min_time'], min_time)

with open('destination_stats', 'w') as file:
    for destination, stats in destination_data.items():
        file.write(f"max_{destination}: {stats['max_time']}\n")
        file.write(f"min_{destination}: {stats['min_time']}\n")
        file.write(",".join(stats['values']) + "\n")
