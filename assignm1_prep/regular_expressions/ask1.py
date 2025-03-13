import re

response = input("Enter text: ")
pattern = r"-?\d+.?\d+"
matches = re.findall(pattern, response)

print(matches)