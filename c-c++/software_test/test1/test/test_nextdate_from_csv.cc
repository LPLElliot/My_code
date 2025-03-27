#include "gtest/gtest.h"
#include "nextdate.h"
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

vector<tuple<int, int, int>> readTestCasesFromCSV(const string &filename)
{
    vector<tuple<int, int, int>> testCases;
    ifstream file(filename);
    string line;

    getline(file, line);

    while (getline(file, line))
    {
        stringstream ss(line);
        string year_str, month_str, day_str;

        getline(ss, year_str, ',');
        getline(ss, month_str, ',');
        getline(ss, day_str, ',');

        int year = stoi(year_str);
        int month = stoi(month_str);
        int day = stoi(day_str);

        testCases.emplace_back(year, month, day);
    }

    return testCases;
}

TEST(NextDateTest, TestFromCSV)
{
    vector<tuple<int, int, int>> testCases = readTestCasesFromCSV("RT_test_data.csv");

    for (const auto &testCase : testCases)
    {
        int year = get<0>(testCase);
        int month = get<1>(testCase);
        int day = get<2>(testCase);

        int initialYear = year;
        int initialMonth = month;
        int initialDay = day;

        NextDate(year, month, day);

        if (ValidDate(initialYear, initialMonth, initialDay))
        {
            int expectedYear = initialYear;
            int expectedMonth = initialMonth;
            int expectedDay = initialDay;

            int daysInMonth[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
            if (LeapYear(expectedYear))
                daysInMonth[2] = 29;

            expectedDay++;
            if (expectedDay > daysInMonth[expectedMonth])
            {
                expectedDay = 1;
                expectedMonth++;
                if (expectedMonth > 12)
                {
                    expectedMonth = 1;
                    expectedYear++;
                }
            }

            ASSERT_EQ(year, expectedYear) << "Input date: " << initialYear << "-" << initialMonth << "-" << initialDay;
            ASSERT_EQ(month, expectedMonth) << "Input date: " << initialYear << "-" << initialMonth << "-" << initialDay;
            ASSERT_EQ(day, expectedDay) << "Input date: " << initialYear << "-" << initialMonth << "-" << initialDay;
        }
        else
        {
            ASSERT_EQ(year, initialYear) << "Input date: " << initialYear << "-" << initialMonth << "-" << initialDay;
            ASSERT_EQ(month, initialMonth) << "Input date: " << initialYear << "-" << initialMonth << "-" << initialDay;
            ASSERT_EQ(day, initialDay) << "Input date: " << initialYear << "-" << initialMonth << "-" << initialDay;
        }
    }
}