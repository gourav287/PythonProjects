# CLI Tracker Application - Command Line Interface Argument Parser
# This module validates command line arguments for the CLI Tracker Application.
import argparse
import datetime

def validDate(date_str):
    """Validate the date format YYYY-MM-DD."""
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise argparse.ArgumentTypeError("Date must be in the format YYYY-MM-DD.")

def validCategory(category_str):
    """Validate the category input."""
    valid_categories = ['water', 'meal', 'activity', 'notes']
    category_str_lower = category_str.lower()
    if category_str_lower not in valid_categories:
        raise argparse.ArgumentTypeError(
            f"Invalid category: {category_str}. Choose from {valid_categories}."
        )
    return category_str_lower

def validDetails(details_str):
    """Validate the details input."""
    if not details_str:
        raise argparse.ArgumentTypeError("Details cannot be empty.")
    return details_str
