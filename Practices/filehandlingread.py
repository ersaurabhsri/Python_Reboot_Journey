f = open('data.txt', 'r')

# data = f.read()       #This will read whole file at a time

# line1=f.readline()    #This will read line by line from file at a time
# line2=f.readline()
# line3=f.readline()
# line4=f.readline()
# line5=f.readline()

# lines=f.readlines()   #READ ALL LINE AND STORES THEM IN A LIST
# print(lines)

for line in f:          #USING FOR LOOP, THIS IS OFTEN BEST WAY TO READLINES BY FILES
    print(line.strip())

# print(line1)
# print(line2)
# print(line3)
# print(line4)
# print(line5)
# print(data)



f.close()
