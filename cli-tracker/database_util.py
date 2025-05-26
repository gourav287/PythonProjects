# CLI Tracker Application - Command Line Interface Argument Parser
# This module works with a JSON file to save, read, and delete entries for the CLI Tracker Application.
import os
import json
import logging
from config import FILEPATH, LOGPATH

logging.basicConfig(filename=LOGPATH, level=logging.INFO, format='%(asctime)s - %(message)s')

def save_entry_to_json(date, category, details):
    # Save the entry to a JSON file.
    if not date or not category or not details:
        logging.error("Error: All fields are required to save an entry.")
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
    
    logging.info(f"Entry added to Database: {entry}")

def read_entries_from_json():
    # Read entries from the JSON file.
    if not os.path.exists(FILEPATH):
        logging.error("No entries found. The database is empty.")
        return []
    with open(FILEPATH, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            logging.error("Error reading the JSON file. It may be corrupted.")
            return []
        if not data:
            logging.error("No entries found. The database is empty.")
            return []
        return data

def delete_entry_from_json(date, category):
    # Delete an entry from the JSON file.
    if not os.path.exists(FILEPATH):
        logging.warning("No entries found. The database is empty.")
        return False
    with open(FILEPATH, 'r+') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            logging.error("Error reading the JSON file. It may be corrupted.")
            data = []
        new_data = [entry for entry in data if not (entry['date'] == date and entry['category'] == category)]
        if len(new_data) == len(data):
            logging.warning(f"No entry found for date: {date} and category: {category}.")
            return False
        file.seek(0)
        file.truncate()
        json.dump(new_data, file, indent=4)
    logging.info(f"Entry deleted for date: {date} and category: {category}.")
    return True

def delete_all_entries_from_json():
    # Delete all entries from the JSON file.
    if not os.path.exists(FILEPATH):
        logging.warning("No entries found. The database is empty.")
        return False
    with open(FILEPATH, 'w') as file:
        json.dump([], file)
    logging.info("All entries deleted from the database.")
    return True
