f = open('data.txt', 'r+')

#data = f.read()
#print(data)

data = f.readline()
print(data)

# Write data in file

f.write("This is new line")
#print(data)   

f.close()
