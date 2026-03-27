# app.py
from utils import add_entry, delete_last_entry, read_entries

add_entry("Project initialized by A")

for line in read_entries():
    print(line)

add_entry('B: first change')
add_entry("A: second change")
add_entry("B: updating logic")
add_entry("A: refining update")

delete_last_entry()
add_entry("B: replaced deleted entry")
print("Executed by A")