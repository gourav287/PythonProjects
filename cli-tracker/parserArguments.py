# CLI Tracker Application - Command Line Interface Argument Parser
# This module defines the command line arguments for the CLI Tracker Application.
import datetime
import validations

def add_parser_arguments(parser):
    parser.add_argument('--date', type=validations.validDate,
                        default=datetime.datetime.today().strftime('%Y-%m-%d'),
                        help='Date for the entry (format: YYYY-MM-DD)')

    parser.add_argument('--category', type=validations.validCategory,
                        required=True,
                        help='Entry category (e.g., water, meal, activity, notes)')

    parser.add_argument('--details', type=validations.validDetails,
                        required=True,
                        help='Add notes or details for this entry')

def view_parser_arguments(parser):
    parser.add_argument('--limit', type=int, default=5,
                        help='Limit the number of entries displayed (default: 5)')

    parser.add_argument('--date', type=validations.validDate,
                        help='Filter by date (format: YYYY-MM-DD)')

    parser.add_argument('--category', type=validations.validCategory,
                        help='Filter by category (e.g., water, meal, activity, notes)')

def parser_arguments(parser, parser_type):
    if parser is None:
        raise ValueError("Parser object is required")
    
    if parser_type == 'add':
        add_parser_arguments(parser)
    elif parser_type == 'view':
        view_parser_arguments(parser)
    else:
        raise ValueError(f"Unknown parser type: {parser_type}. Expected 'add' or 'view'.")