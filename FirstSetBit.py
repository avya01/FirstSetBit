num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

count1 = 0
count2 = 0

while (num1):
    if(num1&1==1):
        count1+=1
    num1>>=1
    
print("Num of set bits in the the first number is ", count1)

while (num2):
    if(num2%1==1):
        count2+=1
    num2>>=1
    
print("Num of set bits in the second number is ", count2)
