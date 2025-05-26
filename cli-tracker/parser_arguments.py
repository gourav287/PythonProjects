# CLI Tracker Application - Command Line Interface Argument Parser
# This module defines the command line arguments for the CLI Tracker Application.
import datetime
import validations

def add_parser_arguments(parser):
    parser.add_argument('--date', type=validations.valid_date,
                        default=datetime.datetime.today().strftime('%Y-%m-%d'),
                        help='Date for the entry (format: YYYY-MM-DD)')

    parser.add_argument('--category', type=validations.valid_category,
                        required=True,
                        help='Entry category (e.g., water, meal, activity, notes)')

    parser.add_argument('--details', type=validations.valid_details,
                        required=True,
                        help='Add notes or details for this entry')

def view_parser_arguments(parser):
    parser.add_argument('--limit', type=int, default=5,
                        help='Limit the number of entries displayed (default: 5)')

    parser.add_argument('--date', type=validations.valid_date,
                        help='Filter by date (format: YYYY-MM-DD)')

    parser.add_argument('--category', type=validations.valid_category,
                        help='Filter by category (e.g., water, meal, activity, notes)')

def delete_parser_arguments(parser):
    parser.add_argument('--date', type=validations.valid_date,
                        # required=True,
                        help='Date of the entry to delete (format: YYYY-MM-DD)')

    parser.add_argument('--category', type=validations.valid_category,
                        # required=True,
                        help='Category of the entry to delete (e.g., water, meal, activity, notes)')
    parser.add_argument('--all', action='store_true',
                        help='Delete all entries in the database')
   
ARGUMENT_FUNCTIONS = {
    'add': add_parser_arguments,
    'view': view_parser_arguments,
    'delete': delete_parser_arguments
}

def parser_arguments(parser, parser_type):
    if parser is None:
        raise ValueError("Parser object is required")
    
    try:
        ARGUMENT_FUNCTIONS[parser_type](parser)
    except KeyError:
        raise ValueError(f"Unknown parser type: {parser_type}. Expected one of {list(ARGUMENT_FUNCTIONS)}")
