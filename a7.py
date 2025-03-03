class Date1:
    months_31_days=(1,3,5,7,8,10)
    months_30_days=(4,6,9,11)

    def __init__(self,d,m,y):
        self.d=d
        self.m=m
        self.y=y

    def returnDate(self):
        return f"{self.d}-{self.m}-{self.y}"

    def __add__(self, other):
        self.d=self.d+1

        if self.m in self.months_31_days and self.m!=12:
            if self.d>31:
                self.d=1
                self.m=self.m+1
        elif self.m==12:
            if self.m==12:
                self.d=1
                self.m=1
                self.y+=1
        elif self.m in self.months_30_days:
            if self.d>30:
                self.d=1
                self.m=self.m+1
        elif self.m==2:
            if self.y%4==0:
                if self.d==30:
                    self.d=1
                    self.m=3
            elif self.y%4!=0:
                if self.d==29:
                    self.d=1
                    self.m=3

d=int(input("\nEnter the Day:"))
m=int(input("Enter the Month:"))
y=int(input("Enter the year:"))

d1=Date1(d,m,y)
d1+1
print(d1.returnDate())
