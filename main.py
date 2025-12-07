# Imports and information
import csv
import os
import datetime
import sys
file1 = "data.csv"
file2 = "figs.csv"
file3 = "sets.csv"
timestamp1 = os.path.getmtime(file1)
timestamp2 = os.path.getmtime(file2)
timestamp3 = os.path.getmtime(file3)
time1 = datetime.datetime.fromtimestamp(timestamp1)
time2 = datetime.datetime.fromtimestamp(timestamp2)
time3 = datetime.datetime.fromtimestamp(timestamp3)
print(f"The last modification date of the ACM data file is {time1}.")
print(f"The last modification date of the Minifigure data file is {time2}.")
print(f"The last modification date of the Set data file is {time3}.")
eur_to_pln = 4.23
usd_to_pln = 3.63
avg_fig_pln = 21.59
# Custom categories built upon the data file
print("1 - Total amount paid for all sets in PLN")
print("2 - Total amount paid for all sets in EUR")
print("3 - Total number of pieces included in sets")
print("4 - Total number of minifigures included in sets")
print("5 - Total retail value of sets with known USD prices")
print("6 - Total retail value of sets with known GBP prices")
print("7 - Total retail value of sets with known EUR prices")
print("8 - Total retail value of sets with known CAD prices")
print("9 - Total amount paid for loose minifigures in PLN")
print("10 - Total amount paid for loose minifigures in EUR")
print("11 - Total amount paid for LEGO in PLN")
print("12 - Total amount paid for LEGO in EUR")
print("13 - End program")
# Variables
# X1
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    x1 = 0
    for row in reader:
        xy1 = row["PricePaid"].strip()
        if xy1:
            x1 += float(xy1)
x1 = round(x1, 2)
# X2
x2 = x1 / eur_to_pln
x2 = round(x2, 2)
# X3
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    x3 = 0
    for row in reader:
        xy3 = row["Pieces"].strip()
        if xy3:
            x3 += float(xy3)
x3 = int(x3)
# X4
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    x4 = 0
    for row in reader:
        xy4 = row["MinifigsInSet"].strip()
        if xy4:
            x4 += float(xy4)
x4 = int(x4)
# X5
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    x5 = 0
    for row in reader:
        xy5 = row["USRetailPrice"].strip()
        if xy5:
            x5 += float(xy5)
x5 = round(x5, 2)
# X6
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    x6 = 0
    for row in reader:
        xy6 = row["UKRetailPrice"].strip()
        if xy6:
            x6 += float(xy6)
x6 = round(x6, 2)
# X7
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    x7 = 0
    for row in reader:
        xy7 = row["DERetailPrice"].strip()
        if xy7:
            x7 += float(xy7)
x7 = round(x7, 2)
# X8
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    x8 = 0
    for row in reader:
        xy8 = row["CARetailPrice"].strip()
        if xy8:
            x8 += float(xy8)
x8 = round(x8, 2)
# X9
with open("figs.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    x9 = 0
    for row in reader:
        xy9 = row["QtyOwnedLoose"].strip()
        if xy9:
            x9 += float(xy9)
x9 = int(x9)
x9 = x9 * avg_fig_pln
x9 = round(x9, 2)
# X10
x10 = x9 / eur_to_pln
x10 = round(x10, 2)
# X11
x11 = x1 + x9
x11 = round(x11, 2)
# X12
x12 = x11 / eur_to_pln
x12 = round(x12, 2)
# 1st inputs and variables
while True:
    try:
        d1 = int(input("What would you like to know? Number: "))
        if 1 <= d1 <= 13:
              break
        else:
              print("Choose a number from the list.")
    except ValueError:
        print("Choose a valid number.")
# 1st choice
if d1 == 1:
    print(f"The total amount is {x1} PLN.")
elif d1 == 2:
    print(f"The total amount is {x2} EUR.")
elif d1 == 3:
    print(f"The total number is {x3} pieces.")
elif d1 == 4:
    print(f"The total number is {x4} minifigures.")
elif d1 == 5:
    print(f"The total value is {x5} USD.")
elif d1 == 6:
    print(f"The total value is {x6} GBP.")
elif d1 == 7:
    print(f"The total value is {x7} EUR.")
elif d1 == 8:
    print(f"The total value is {x8} CAD.")
elif d1 == 9:
    print(f"The total amount is {x9} PLN.")
elif d1 == 10:
    print(f"The total amount is {x10} EUR.")
elif d1 == 11:
    print(f"The total amount is {x11} PLN.")
elif d1 == 12:
    print(f"The total amount is {x12} EUR.")
elif d1 == 13:
    sys.exit()
# End of code