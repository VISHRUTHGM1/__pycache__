print("Enter 3 Numbers")
onum = int(input("Enter Number 1:"))
tnum = int(input("Enter Number 2:"))
thnum = int(input("Enter Number 3:"))
tem = thnum 
thnum = tnum
tnum = onum
onum = tem 
print(f"The numbers after swapping are: 1st number is {onum}, 2nd number is {tnum}, 3rd number is {thnum}")
