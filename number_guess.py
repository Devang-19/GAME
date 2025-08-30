import random as r

text = (" Number Guessing Game ")
print(text.center(120,'='))

attempts_count = 0
count = 3
number = r.randint(1,20)
# print(number)

for i in range(1,count+1):

    print("Attempt",i,"of",count)
    gussed_number = int(input("Enter the Number : "))
   
    if gussed_number == number:
        print("Congratulations... You've Gussed the Correct Number !!!")
        break

    else:
        print("Try Again ! Incorrect Guess")


if i == count:
    print("Correct Number is : ",number)