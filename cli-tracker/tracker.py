# CLI Tracker Application - Command Line Interface Argument Parser
# This is the main entry point for the CLI Tracker Application.
# This module initializes the command line argument parser and handles the main functionality of the application.
import argparse
import parserArguments
import databaseUtil

def main():
    parser = argparse.ArgumentParser(description="CLI Tracker Application")
    parser.add_argument('--version', action='version',
                    version='CLI Tracker Application Version 1.0',
                    help='Show the version of the CLI Tracker Application')
    subParsers = parser.add_subparsers(dest='command', required=True)

    addParser = subParsers.add_parser('add', help='Add a new entry')
    parserArguments.parser_arguments(addParser, 'add')

    viewParser = subParsers.add_parser('view', help='View all entries')
    parserArguments.parser_arguments(viewParser, 'view')

    args = parser.parse_args()

    if args.command == 'add':
        print(f"Adding entry on {args.date} with category '{args.category}' and details '{args.details}'")
        databaseUtil.saveEntryToJson(args.date, args.category, args.details)

    elif args.command == 'view':
        entries = databaseUtil.readEntriesFromJson()
        if args.date:
            entries = [entry for entry in entries if entry['date'] == args.date]
        if args.category:
            entries = [entry for entry in entries if entry['category'] == args.category]
        limit = args.limit if hasattr(args, 'limit') else None
        if limit is not None:
            entries = entries[:limit]
        if entries:
            print("Entries in the CLI Tracker Application:")
            for entry in entries:
                print(f"Date: {entry['date']}, Category: {entry['category']}, Details: {entry['details']}")
        else:
            print("No entries found in the CLI Tracker Application with the specified filters.")

if __name__ == "__main__":
    main()
