import re

txt = "this is a text that includes youtube@gmail.com email address wow even amazon@twitch.tv exists and even discord@service.com"
#pattern = r"\[a-z][A-Z]+\@\c+.\c+"
matches = re.findall(pattern, txt)
print(matches)