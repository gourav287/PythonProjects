"""
GET EMPLOYEE MAIL FROM NAME

You are given a csv file containing list of Employee Names working in the company xyz.
The company uses standard email pattern of a-b.c@xyz.com where "a b c" is the name of the person.
Create a CSV file containing names and email addresses of all the employees.

Input: A CSV file containing employee names
Output: A CSV file containing employee names and email addresses

Eg.
Input 1: John Doe
Expected Output 1: John Doe, john.doe@xyz.com

Input 2: John Michael Doe
Expected Output 2: john-michael.doe@xyz.com

Input 3: John Michael Doe Jr
Expected Output 3: john-michael-doe.jr@xyz.com
"""


#Solution
import pandas as pd

# Define necessary variables
domain = "@xyz.com"
outputDct = {"Name": [], "Email Id": []}
inputFile = "inputNames.csv"
outputFile = "employeeMail.csv"

# Retrieve the data points
df = pd.read_csv(inputFile)
outputDct["Name"] = df["Display Name"].tolist()
names = [name.lower() for name in outputDct["Name"]]

# Apply the required operation and save the results
for i in range(len(names)):
    name = list(map(str, names[i].split()))
    outputDct["Email Id"].append("-".join(name[:-1]) + "." + name[-1] + domain)

# Output the results into a new csv
outputdf = pd.DataFrame(outputDct)
outputdf.to_csv(outputFile, index=False)