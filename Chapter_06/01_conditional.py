a = int(input ("Enter your age: "))

# if else statement

if(a>=18):
    print("you are above the age of consent")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering 0 Which is not a valid age")

else: 
    print("You are below the age of consent")  

print("End of Program")