#accept line numbers frm user and print the output:
i=int(input("Enter the line numbers:"))
for i in range(1,i+1):
    for j in range(1,i+1):
        print("*",end='\t')
        print()

#Swapping:
print("Enter two numbers for swapping:")
num1=int(input("num1="))
num2=int(input("num2="))
print("Number before swapping\nnum1=",num1,"\nnum2=",num2)
num1,num2=num2,num1
print("Numbers after swapping\nnum1=",num1,"\nnum2=",num2)

#accept two number from user and perform following operations:+,-,*,/,//
print("Enter two numbers:")
num1=int(input("num1="))
num2=int(input("num2="))
print("addition=",num1+num2,"\nsubstraction=",num1-num2,"\nmultiplication=",num1*num2,"\ndivision=",num1/num2)
mod=num1//num2
print("mmodulo division=",mod,end="\n")
