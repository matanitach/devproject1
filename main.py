import json
import os

def read_sensor_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def average_temperature(sensor_data):
    temps = [entry['temperature'] for entry in sensor_data]
    return sum(temps) / len(temps)

def main():
    print("Current working directory:", os.getcwd())
    file_path = 'sensor_data.json'
    data = read_sensor_data(file_path)
    avg_temp = average_temperature(data)
    print(f"Average Temperature: {avg_temp:.2f}°C")
    print("test automation!")
if __name__ == "__main__":
    main()
