# CLI Tracker Application - Command Line Interface Argument Parser
# This module defines the command line arguments for the CLI Tracker Application.
import datetime
import validations

def addParserArguments(parser, argumentVal, actionVal="store", helpVal=None, 
                       defaultVal=None, typeVal=None, versionVal=None, requiredVal=False):
    kwargs = {
        'action': actionVal,
    }
    if helpVal is not None:
        kwargs['help'] = helpVal
    if defaultVal is not None:
        kwargs['default'] = defaultVal
    if typeVal is not None:
        kwargs['type'] = typeVal
    if versionVal is not None:
        kwargs['version'] = versionVal
    if requiredVal:
        kwargs['required'] = requiredVal
    parser.add_argument(argumentVal, **kwargs)

def parserArguments(parser=None):
    # Parse command line arguments for the CLI Tracker Application.
    addParserArguments(parser, "--version", 
                       actionVal="version", 
                       helpVal="Show the version of the CLI Tracker Application",
                       versionVal="CLI Tracker Application Version 1.0")
    
    addParserArguments(parser, "--date",
                       helpVal="Specify the date for the CLI Tracker Application (format: YYYY-MM-DD)", 
                       defaultVal=datetime.datetime.today().strftime("%Y-%m-%d"), 
                       typeVal=validations.validDate)
    
    addParserArguments(parser, "--category",
                       helpVal="Specify the category for the Tracker Application (e.g., 'water', 'meal', 'activity', 'notes')", 
                       typeVal=validations.validCategory,
                       requiredVal=True)
    
    addParserArguments(parser, "--details",
                       helpVal="Show detailed information about the CLI Tracker Application",
                       typeVal=validations.validDetails,
                       requiredVal=True)
    
    return parser.parse_args()