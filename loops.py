#write a program to find the sum of even number upto 50
sum = 0
for i in range(1,51):
    if(i % 2 == 0):
        sum += i
print("sum of even number ",sum)

#write a program to write the first 20 number and their square
for i in range(1,21):
    print(i , i* i)
#write a program to find sum of first 10 odd number using while loop
sum = 0
n=0
while n<=20:
    if n % 2 != 0:
        sum += n
    n += 1
print("sum of odd number ",sum)

#write a program to check if a number is dvisble by 8 and 11 upto 100
num = int(input("Enter a number: "))
if(num % 8 == 0 and num % 11 == 0):
    print("The is divisible by both 8 and 11")
else:
    print("The is not divisible by both 8 and 11")





