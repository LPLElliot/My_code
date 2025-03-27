#include "gtest/gtest.h"
#include "nextdate.h"

TEST(NextDateTest, SimpleTest)
{
    int year = 2023, month = 10, day = 26;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2023);
    ASSERT_EQ(month, 10);
    ASSERT_EQ(day, 27);
}

TEST(NextDateTest, EndOfMonthTest)
{
    int year = 2023, month = 10, day = 31;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2023);
    ASSERT_EQ(month, 11);
    ASSERT_EQ(day, 1);
}

TEST(NextDateTest, EndOfYearTest)
{
    int year = 2023, month = 12, day = 31;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2024);
    ASSERT_EQ(month, 1);
    ASSERT_EQ(day, 1);
}

TEST(NextDateTest, LeapYearTest)
{
    int year = 2024, month = 2, day = 29;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2024);
    ASSERT_EQ(month, 3);
    ASSERT_EQ(day, 1);
}

TEST(NextDateTest, NonLeapYearTest)
{
    int year = 2023, month = 2, day = 28;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2023);
    ASSERT_EQ(month, 3);
    ASSERT_EQ(day, 1);
}

TEST(NextDateTest, InvalidDateTest)
{
    int year = 2023, month = 2, day = 30;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2023);
    ASSERT_EQ(month, 2);
    ASSERT_EQ(day, 30);
}