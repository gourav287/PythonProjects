# CLI Tracker Application - Command Line Interface Argument Parser
# This module works with a JSON file to save, read, and delete entries for the CLI Tracker Application.
import os
import json

FILEPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cli_tracker.json")

def saveEntryToJson(date, category, details):
    # Save the entry to a JSON file.
    if not date or not category or not details:
        print("Error: All fields are required to save an entry.")
        return
    if not os.path.exists(FILEPATH):
        with open(FILEPATH, 'w') as file:
            json.dump([], file)
    with open(FILEPATH, 'r+') as file:
        data = json.load(file)
        entry = {
            "date": date,
            "category": category,
            "details": details
        }
        data.append(entry)
        file.seek(0)
        json.dump(data, file, indent=4)
    

    print(f"Entry saved to Database: \nDate: {date}, \nCategory: {category}, \nDetails: {details}")

def readEntriesFromJson():
    # Read entries from the JSON file.
    if not os.path.exists(FILEPATH):
        print("No entries found. The database is empty.")
        return []
    with open(FILEPATH, 'r') as file:
        data = json.load(file)
        if not data:
            print("No entries found. The database is empty.")
            return []
        return data

def deleteEntryFromJson(date, category):
    # Delete an entry from the JSON file.
    if not os.path.exists(FILEPATH):
        print("No entries found. The database is empty.")
        return
    with open(FILEPATH, 'r+') as file:
        data = json.load(file)
        new_data = [entry for entry in data if not (entry['date'] == date and entry['category'] == category)]
        if len(new_data) == len(data):
            print(f"No entry found for date: {date} and category: {category}.")
            return
        file.seek(0)
        file.truncate()
        json.dump(new_data, file, indent=4)
    print(f"Entry deleted for date: {date} and category: {category}.")