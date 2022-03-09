import re

string = "Hey!! why it's called python???"
new_string = re.sub(r"[^a-zA-Z0-9]" ," " ,string)
print(new_string)
