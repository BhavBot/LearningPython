import re

pattern = 'a...s'
test_string = 'abyss alias'
result = re.match(pattern, test_string)
print(result)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	