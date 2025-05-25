# CLI Tracker Application - Command Line Interface Argument Parser
# This is the main entry point for the CLI Tracker Application.
# This module initializes the command line argument parser and handles the main functionality of the application.
import argparse
import parserArguments
import databaseUtil

# FILENAME = "cli_tracker.json"

parser = argparse.ArgumentParser(description="CLI Tracker Application")
subParser = parser.add_subparsers(dest='add')

args = parserArguments.parserArguments(parser)

def main():

    print(f"CLI Tracker Application started on {args.date}")
    databaseUtil.saveEntryToJson(args.date, args.category, args.details)
    # Here you can add the main functionality of your CLI Tracker Application
if __name__ == "__main__":
    main()
