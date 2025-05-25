# CLI Tracker Application - Command Line Interface Argument Parser
# This module works with a JSON file to save, read, and delete entries for the CLI Tracker Application.
import os
import json
import logging

DIRPATH = os.path.dirname(os.path.abspath(__file__))
FILEPATH = os.path.join(DIRPATH, "cli_tracker.json")
LOGPATH = os.path.join(DIRPATH, "tracker.log")

logging.basicConfig(filename=LOGPATH, level=logging.INFO, format='%(asctime)s - %(message)s')

def saveEntryToJson(date, category, details):
    # Save the entry to a JSON file.
    if not date or not category or not details:
        print("Error: All fields are required to save an entry.")
        return
    if not os.path.exists(FILEPATH):
        with open(FILEPATH, 'w') as file:
            json.dump([], file)
    with open(FILEPATH, 'r+') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
        entry = {
            "date": date,
            "category": category,
            "details": details
        }
        data.append(entry)
        file.seek(0)
        json.dump(data, file, indent=4)
    

    print(f"Entry saved to Database: \nDate: {date}, \nCategory: {category}, \nDetails: {details}")
    logging.info(f"Entry added: {entry}")

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