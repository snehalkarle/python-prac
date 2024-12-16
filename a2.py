list1=[]
def addDigit(n):
    while n > 9:
        sum = 0
        while n > 0:
            rem = n % 10
            sum += rem
            n = n // 10
        n = sum
    return n

def additionList(list1):      
    list2=[]
    for i in list1:
        n=addDigit(i)
        list2.append(n)
    return list2

ch=input("Do you want to add the no in list(yes/no) ")
ch=ch.lower()
while ch=="yes":
    a=int(input("Enter the number "))
    list1.append(a)
    ch=input("Do you want to add the no in list(yes/no) ")
    ch=ch.lower()

if len(list1)==0:
    print("There is no elements in list")
else:
    print(additionList(list1))
