age = int(input("Enter the your age: "))

if(age>=18):
    print("You are an adult and your age is :",age)

elif(age==0):
    print("You are entering 0 which is not valid age")

elif(age<0):
    print("You are entering 0 or invalid age")

else:
    print("You are the below age of consent")

print("End of Program")