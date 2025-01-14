#logic building formula

#step1
#user i/p datatype - int
# o/p - string if he can go to club or not

#step2 rough logic(brute force logic)
#age 21 > print can go
#age 21 < print can not go

#step3 logic
age = int(input("Enter the age\n"))

if age >= 21:
    print("Can go to club")
else:
    print("Cant get in")

#step4 check for the edge cases
#step5 optimize code