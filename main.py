
import datetime
import json

# define the list of indicators to track
indicators = ["Smoking", "Exercise", "Meditation"]

# load the metadata file if it exists, otherwise create a new empty dictionary
try:
    with open("metadata.json", "r") as f:
        metadata = json.load(f)
except FileNotFoundError:
except FileNotFoundError:
    metadata = {}

# define the function to add a new indicator
def add_indicator():
    # ask the user for the new indicator name
    name = input("Enter the name of the new indicator: ")
    # ask the user for any additional metadata
    metadata[name] = {}
    while True:
        key = input("Enter a metadata key (or leave blank to finish): ")
        if not key:
            break
        value = input("Enter the metadata value: ")
        metadata[name][key] = value
    # save the metadata to file
    with open("metadata.json", "w") as f:
        json.dump(metadata, f)

# define the function to log an indicator
def log_indicator(name):
    # ask the user if they participated in the indicator today
    answer = input(f"Did you participate in {name} today? (y/n): ")
    if answer.lower() == "y":
        # ask the user how many times they participated
        count = input("How many times did you participate?: ")
        # log the indicator with timestamp and count
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        if name not in metadata:
            metadata[name] = {}
        metadata[name][today] = {"count": int(count)}
        # save the metadata to file
        with open("metadata.json", "w") as f:
            json.dump(metadata, f)

# check if it's a new day and ask the user to log the indicators
today = datetime.datetime.now().strftime("%Y-%m-%d")
if today not in metadata.get("last_logged", []):
    for name in indicators:
        log_indicator(name)
    # update the last_logged metadata
    if "last_logged" not in metadata:
        metadata["last_logged"] = []
    metadata["last_logged"].append(today)
    # save the metadata to file
    with open("metadata.json", "w") as f:
        json.dump(metadata, f)

# define the function to view the logged data for an indicator
def view_indicator(name):
    if name not in metadata:
        print(f"No data found for {name}.")
        return
    # print the user-defined metadata for the indicator
    print(f"Metadata for {name}:")
    for key, value in metadata[name].items():
        if key != "count":
            print(f"  {key}: {value}")
    # print the daily participation counts for the indicator
    print(f"Daily counts for {name}:")
    for key, value in metadata[name].items():
        if key != "count":
            print(f"  {key}: {value['count']}")

# define the function to analyze the logged data for an indicator
def analyze_indicator(name):
    if name not in metadata:
        print(f"No data found for {name}.")
        return
    # calculate the total and average participation counts for the indicator
    total_count = 0
    count = 0
    for key, value in metadata[name].items():
        if key != "count":
            total_count += value["count"]
            count += 1
    if count == 0:
        print(f"No data found for {name}.")
    else:
        avg_count = total_count / count
        print(f"Total {name} count: {total_count}")
        print(f"Average {name} count per day: {avg_count:.2f}")

# define the function to view and analyze all indicators
def view_all():
    for name in indicators:
        print(f"=== {name} ===")
        view_indicator(name)
        analyze_indicator(name)
        print()

# ask the user for the command to execute
while True:
    command = input("Enter a command (add, view, analyze, exit): ")
    if command == "add":
        add_indicator()
    elif command == "view":
        name = input("Enter the name of the indicator to view: ")
        view_indicator(name)
    elif command == "analyze":
        name = input("Enter the name of the indicator to analyze: ")
        analyze_indicator(name)
    elif command == "exit":
        break
    else:
        print("Invalid command. Please try again.")

# save the metadata to file
with open("metadata.json", "w") as f:
    json.dump(metadata, f)