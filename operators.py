#write a program to check if the number is positive
num = int(input("enter a number: "))
if num>0:
    print("number is postive")
else:
    print("number is negative")

#wirte a program to check if the number is odd or even
num = int(input("enter a number: "))
if (num %2 ==0):
    print("number is even")
else:
    print("number is odd")

#write a program check whether the passed letter is a vowel or not
print("Enter a letter:")
letter = input()
if (letter not in "aeiou"):
    print("not a vowel")
else:
    print("its a vowel")

#write a program to create area calculator
print("press 1 to get the area of square")
print("press 2 to get the area of rectangle")
print("press 3 to get the area of triangle")
print("press 4 to get the area of circle")
number = int(input("Enter the number:"))
if (number == 1):
    num = int(input("Enter the number:"))
    print("The area of square is: ",num**2)
elif (number == 2):
    num = int(input("Enter the length:"))
    num1= int(input("Enter the width:"))
    print("The area of rectangle is: ",num*num1)
elif (number == 3):
    num = int(input("Enter the breadth:"))
    num1= int(input("Enter the height:"))
    print("The area of triangle is: ",1/2*num*num1)
elif (number == 4):
    num = int(input("Enter the radius:"))
    print("The area of circle is: ",22/7*num*num)
else:
    print("Enter a valid number")

#write a program to check if a number enter is a single digit number , 2-digit number till 5-digit
num = int(input("Enter the till 5 digit number:"))
if (num > 0 and num <= 9):
    print("It is single digit number")
elif(num > 9 and num <= 99   ):
    print("It is double digit number")
elif(num > 99 and num <= 999  ):
    print("It is three digit number")
elif(num > 999 and num <= 9999  ):
    print("It is four digit number")
elif(num > 9999 and num <= 99999  ):
    print("It is five digit number")






