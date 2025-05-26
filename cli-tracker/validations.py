# CLI Tracker Application - Command Line Interface Argument Parser
# This module validates command line arguments for the CLI Tracker Application.
import argparse
import datetime
from config import VALID_CATEGORIES

def valid_date(date_str):
    """Validate the date format YYYY-MM-DD."""
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise argparse.ArgumentTypeError("Date must be in the format YYYY-MM-DD.")

def valid_category(category_str):
    """Validate the category input."""
    category_str_lower = category_str.lower()
    if category_str_lower not in VALID_CATEGORIES:
        raise argparse.ArgumentTypeError(
            f"Invalid category: {category_str}. Choose from {VALID_CATEGORIES}."
        )
    return category_str_lower

def valid_details(details_str):
    """Validate the details input."""
    if not details_str:
        raise argparse.ArgumentTypeError("Details cannot be empty.")
    return details_str
