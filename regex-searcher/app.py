"""
    In this problem, we are trying to find the first sub-string in single quotes 
    which is preceeded after a given sub-string as part of the same string
    eg: string              = "I 'like' playing cricket in 'the' evening"
    preceeding substring    = "playing"
    result                  = "the"
    Explanation:Though both 'like' and 'the' are in single quotes, 
                only the substring 'the' is preceeded by 'playing'
"""
import re

# Example text: "The quick brown fox 'jumps' over the 'lazy' dog"
text = input("Please input the text string: ")

# Input the preceeding substring
preceeding_subs = input("Please input the preceeding substring: ")

# Search for the string in single quotes after the preceeding substring
pattern = rf"{preceeding_subs}[^']*'([^']+)'"

# Find the match
match = re.search(pattern, text)

# Extract the matched string
if match:
    result = match.group(1)
    print("The required single-quoted substring is:", result)
else:
    print("No match found for the given input.")