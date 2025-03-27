import random
import csv

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 0  

def generate_test_cases(num_cases=100, filename="RT_test_data.csv"):
    test_cases = []
    for _ in range(num_cases):
        year = random.randint(1800, 2200)
        month = random.randint(1, 12)
        day = random.randint(1, days_in_month(year, month))
        test_cases.append([year, month, day])

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['year', 'month', 'day'])  
        writer.writerows(test_cases)

if __name__ == "__main__":
    generate_test_cases()
    print("Test cases generated and saved to RT_test_data.csv")