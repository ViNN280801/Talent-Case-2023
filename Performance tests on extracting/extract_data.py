import json, time, csv

exec_times = []

for _ in range(10000):
    start_time = time.time()
    
    # Open the JSON file and load its contents
    with open("sample.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    # Extract the "text" values
    text_values = [entry["text"] for entry in data]

    # Write the "text" values to a .txt file
    with open("sentences.txt", "w", encoding="utf-8") as file:
        for text in text_values:
            file.write(text + "\n")
            
    # Adding each time to the list
    exec_times.append(time.time() - start_time)
    
# Write the execution times to a CSV file
with open("execution_times_py.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Execution Time (seconds)"])
    for time in exec_times:
        writer.writerow([time])
