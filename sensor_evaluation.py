import pandas as pd
import statistics
import json
from datetime import datetime
import sys

def parse_log_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    reference = list(map(float, lines[0].split()[1:]))
    sensors = {}
    current_sensor_type = None
    current_sensor_name = None

    for line in lines[1:]:
        split_line = line.split()

        if not split_line:  # Skip empty lines
            continue
        
        # Check if the first entry is a date
        try:
            datetime.strptime(split_line[0], '%Y-%m-%dT%H:%M')
            is_date = True
        except ValueError:
            is_date = False

        if is_date:
            time, value = split_line[0], split_line[1]
            sensors[current_sensor_type][current_sensor_name].append(float(value))
        else:
            current_sensor_type, current_sensor_name = split_line
            if current_sensor_type not in sensors:
                sensors[current_sensor_type] = {}
            if current_sensor_name not in sensors[current_sensor_type]:
                sensors[current_sensor_type][current_sensor_name] = []

    print(f"Parsed sensors data: {sensors}")  # Added print statement to check parsed data.
    return reference, sensors

def evaluate_sensors(reference, sensors):
    results = {}
    for sensor_type, sensor_data in sensors.items():
        for sensor, measurements in sensor_data.items():
            if not measurements:
                print(f"No measurements for sensor: {sensor}")
                continue
            if sensor_type == 'thermometer':
                mean = statistics.mean(measurements)
                stdev = statistics.stdev(measurements)
                if abs(mean - reference[0]) <= 0.5:
                    if stdev < 3:
                        results[sensor] = "ultra precise"
                    elif stdev < 5:
                        results[sensor] = "very precise"
                    else:
                        results[sensor] = "precise"
                else:
                    results[sensor] = "precise"
            elif sensor_type == 'humidity':
                if all(abs(m - reference[1]) <= 1 for m in measurements):
                    results[sensor] = "keep"
                else:
                    results[sensor] = "discard"

    return results

def main():
    if len(sys.argv) != 3:
        print("Usage: sensor_evaluation.py [input file] [output file]")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    reference, sensors = parse_log_file(input_file_path)

    results = evaluate_sensors(reference, sensors)

    with open(output_file_path, 'w') as outfile:
        json.dump(results, outfile, indent=4)

if __name__ == "__main__":
    main()

