a = int(input("Enter the your age: "))

# IF statement no 1
if(a%2 == 0):
    print("a is even")
# End of IF statement no 2

# IF statement no 2
elif(a>=18):
    print("You are above the age of consent")
    print("Good for You")

elif(a<0):
    print("You are entering an invalid negative age")

else:
    print("You are the below age of consent")

# End of IF statement no 2

print("End of Program")