import os

DIRPATH = os.path.dirname(os.path.abspath(__file__))
FILEPATH = os.path.join(DIRPATH, "cli_tracker.json")
LOGPATH = os.path.join(DIRPATH, "tracker.log")
VALID_CATEGORIES = ['water', 'meal', 'activity', 'notes']