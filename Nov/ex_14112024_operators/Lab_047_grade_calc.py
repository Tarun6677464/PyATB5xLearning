score = int(input("Enter your score\n"))

if score >= 90 and score <= 100:
    print("Your grade is A")
elif score >=80 and score <= 89:
    print("your grade is B")
elif score >=70 and score <= 79:
    print("your grade is C")
elif score >=60 and score <= 69:
    print("your grade is D")
else:
    print("Your grade is F")