count = 0
line = str(input("Enter you line :\n"))
for i in line:
    if i.isspace():
        count = count + 1

print(f"There are {count} whitespaces in the line")

print(f'There are {len(line)} characters ')
words = count + 1
print(f"There are {words} words")
