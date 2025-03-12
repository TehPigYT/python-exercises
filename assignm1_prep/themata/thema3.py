import re

pattern = r"\d+"
string = "23109u3429jvwenfsinwesignesngsn"

matches = re.findall(pattern, string)

print(matches)
