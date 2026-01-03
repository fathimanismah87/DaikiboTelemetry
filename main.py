import json
from datetime import datetime

# Function to convert ISO string to milliseconds
def iso_to_milliseconds(iso_str):
    dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)

# Function to process data-1.json (already in milliseconds)
def process_data1():
    with open("data1.json", "r") as f:
        data1 = json.load(f)
    # Already in correct format, return as is
    return data1

# Function to process data-2.json (ISO timestamps)
def process_data2():
    with open("data2.json", "r") as f:
        data2 = json.load(f)
    for item in data2:
        item["timestamp"] = iso_to_milliseconds(item["timestamp"])
    return data2

# Main function to merge data
def main():
    unified_data = []
    unified_data.extend(process_data1())
    unified_data.extend(process_data2())
    
    # Optional: Save the result to data-result.json
    with open("data-result.json", "w") as f:
        json.dump(unified_data, f, indent=2)
    
    # Print unified data
    print(json.dumps(unified_data, indent=2))

# Run the program
if __name__ == "__main__":
    main()
