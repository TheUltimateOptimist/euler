def is_leap_year(year: int) -> int:
    if year % 4 != 0:
        return False
    if year % 100 == 0 and year % 400 != 0:
        return False
    return True

def days_in_month(month: int, is_leap: bool = False) -> int:
    if month in (4, 6, 9, 11):
        return 30
    if month == 2:
        return 29 if is_leap else 28
    return 31

def firstMonthSundays() -> int:
    count = 0
    days_passed = 0
    for year in range(1900, 2001):
        for month in range(1, 13):
            if year > 1900 and days_passed % 7 == 6:
                count += 1
            days_passed += days_in_month(month, is_leap_year(year))
    return count

print(f"The number of sundays on the first of the month is:\n{firstMonthSundays()}")
