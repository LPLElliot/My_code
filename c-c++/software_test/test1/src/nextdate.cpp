#include <iostream>

bool LeapYear(int year)
{
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

bool ValidDate(int year, int month, int day)
{
    if (year < 1800 || year > 2200)
        return false;
    if (month < 1 || month > 12)
        return false;
    if (day < 1)
        return false;

    int daysInMonth[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    if (LeapYear(year))
        daysInMonth[2] = 29;

    if (day > daysInMonth[month])
        return false;

    return true;
}

void NextDate(int &year, int &month, int &day)
{
    if (!ValidDate(year, month, day))
    {
        return; // 或者抛出异常，根据你的需求
    }
    else
    {
        if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10)
        {
            if (day == 31)
            {
                month++;
                day = 1;
            }
            else
            {
                day++;
            }
        }
        else if (month == 4 || month == 6 || month == 9 || month == 11)
        {
            if (day == 30)
            {
                month++;
                day = 1;
            }
            else
            {
                day++;
            }
        }
        else if (month == 12)
        {
            if (day == 31)
            {
                year++;
                month = 1;
                day = 1;
            }
            else
            {
                day++;
            }
        }
        else
        {
            if ((LeapYear(year) && day == 29) || (!LeapYear(year) && day == 28))
            {
                month++;
                day = 1;
            }
            else
            {
                day++;
            }
        }
    }
}