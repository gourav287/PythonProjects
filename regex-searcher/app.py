import re

# Example text
text = "The quick brown fox 'jumps' over the 'lazy' dog"

# Search for the string in single quotes after "quick"
pattern = r"(?<=quick\s')[^']*"

# Find the match
match = re.search(pattern, text)

# Extract the matched string
if match:
    result = match.group(0)
    print(result)