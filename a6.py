
class Time:
    def __init__(self, hrs=0, mins=0):
        self.hrs = hrs
        self.mins = mins
        self.normalize_time()

    def normalize_time(self):
        self.hrs += self.mins // 60
        self.mins = self.mins % 60

    def __add__(self, other):
        total_hrs = self.hrs + other.hrs
        total_mins = self.mins + other.mins
        return Time(total_hrs, total_mins)

    def __sub__(self, other):
        total_mins_1 = self.hrs * 60 + self.mins
        total_mins_2 = other.hrs * 60 + other.mins
        diff_mins = abs(total_mins_1 - total_mins_2)
        return Time(diff_mins // 60, diff_mins % 60)

    def __mul__(self, times):
        total_mins = (self.hrs * 60 + self.mins) * times
        return Time(total_mins // 60, total_mins % 60)

    def __str__(self):
        return f"{self.hrs} hrs, {self.mins} minutes"

def get_time_input():
    hrs = int(input("Enter hours: "))
    mins = int(input("Enter minutes: "))
    return Time(hrs, mins)

print("Enter time for process P1:")
p1 = get_time_input()

print("Enter time for process P2:")
p2 = get_time_input()

total_time = p1 + p2
print(f"Total time for both processes: {total_time}")

time_diff = p2 - p1
print(f"Difference between P2 and P1: {time_diff}")

times = int(input("Enter the multiplier for P1: "))
multiple_time = p1 * times
print(f"{times} times of P1: {multiple_time}")
