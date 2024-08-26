#if you have a medical cause y or n \
#if yes then alowed to take exam
#if it is no the you have to check attendence 
#if attendence is greater than 75 the allow 
#if it is no then not allowed
criteria1 = input("Do you have a medical cause?:")
if criteria1.lower() == "yes":
    print("You are allowed to take exam.")
elif criteria1.lower() == "no":
    attendance = int(input("Please enter your attendence rate:"))
    if attendance >= 75:
        print("You are allowed to take the test.")
    else:
        print("You aren't allowed to take the test.")
else:
    print("Try Again")
