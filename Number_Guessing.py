#number guessing
password =7
for i in range(3):
    user=int(input("please guess the number"))

    if user ==password:
        print("Correct")
        
    else:
        print ("You are wrong!!!, please try again")