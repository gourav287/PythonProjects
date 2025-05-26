# CLI Tracker Application - Command Line Interface Argument Parser
# This is the main entry point for the CLI Tracker Application.
# This module initializes the command line argument parser and handles the main functionality of the application.
import argparse
import parser_arguments
import database_util
import logging
from config import LOGPATH

logging.basicConfig(filename=LOGPATH, level=logging.INFO, format='%(asctime)s - %(message)s')

def display_entries(entries):
    if entries:
        print("Entries in the CLI Tracker Application:")
        for entry in entries:
            print(f"Date: {entry['date']}, Category: {entry['category']}, Details: {entry['details']}")
        logging.info(f"Displayed {len(entries)} entries successfully.")
    else:
        print("No entries found in the CLI Tracker Application with the specified filters.")
        logging.warning("No entries found in the CLI Tracker Application with the specified filters.")

def main():
    parser = argparse.ArgumentParser(description="CLI Tracker Application")
    parser.add_argument('--version', action='version',
                    version='CLI Tracker Application Version 1.0',
                    help='Show the version of the CLI Tracker Application')
    sub_parsers = parser.add_subparsers(dest='command', required=True)

    add_command_parser = sub_parsers.add_parser('add', help='Add a new entry')
    parser_arguments.parser_arguments(add_command_parser, 'add')

    view_command_parser = sub_parsers.add_parser('view', help='View all entries')
    parser_arguments.parser_arguments(view_command_parser, 'view')

    delete_command_parser = sub_parsers.add_parser('delete', help='Delete entries')
    parser_arguments.parser_arguments(delete_command_parser, 'delete')

    args = parser.parse_args()

    if args.command == 'add':
        logging.info(f"Adding entry on {args.date} with category '{args.category}' and details '{args.details}'")
        database_util.save_entry_to_json(args.date, args.category, args.details)

    elif args.command == 'view':
        logging.info("Viewing entries in the database.")
        try:
            entries = database_util.read_entries_from_json()
            if args.date:
                entries = [entry for entry in entries if entry['date'] == args.date]
            if args.category:
                entries = [entry for entry in entries if entry['category'] == args.category]
            limit = args.limit if hasattr(args, 'limit') else None
            if limit is not None:
                entries = entries[:limit]
            display_entries(entries)
        except FileNotFoundError:
            print("No entries found. The database is empty.")
            logging.error("No entries found. The database is empty.")
        except Exception as e:
            print(f"An error occurred while reading the database: {e}")
            logging.error(f"An error occurred while reading the database: {e}")
    elif args.command == 'delete':
        deleted = False
        if args.all:
            logging.info("Deleting all entries in the database")
            deleted = database_util.delete_all_entries_from_json()
        elif args.date and args.category:
            logging.info(f"Deleting entry on {args.date} with category '{args.category}'")
            deleted = database_util.delete_entry_from_json(args.date, args.category)
        else:
            print("Please specify --all or both --date and --category to delete.")
            logging.error("--all or both --date and --category are required to delete some/all entries.")

        if not deleted:
            print(f"Failed to delete entries from the database.")
            logging.error("Failed to delete entries from the database.")
    else:
        print("Unknown command. Please use 'add', 'view', or 'delete'.")

if __name__ == "__main__":
    main()
