# Writing a file in Python, there are mainly 3 common ways/modes used:
lines=["Hello\n","Python\n","File handling\n"]

f = open("writedata.txt","w")

# f.write("This is 2nd line")
f.writelines(lines)
