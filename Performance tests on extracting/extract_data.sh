#!/bin/bash

# Number of iterations
num_iterations=1000

# Create an array to store execution times
exec_times=()

for ((i = 1; i <= $num_iterations; i++)); do
    start_time=$(date +%s%N)

    jq -r '.[].text' sample.json >sentences.txt

    end_time=$(date +%s%N)

    # Calculate the execution time in seconds
    execution_time=$(echo "scale=6; ($end_time - $start_time) / 1000000000" | bc)

    # Append the execution time to the array
    exec_times+=($execution_time)
done

# Write the execution times to a CSV file
echo "Execution Time (seconds)" >execution_times_bash.csv
for time in "${exec_times[@]}"; do
    echo "$time" >>execution_times_bash.csv
done
