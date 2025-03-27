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

TEST(ValidDateTest, ValidDate)
{
    ASSERT_TRUE(ValidDate(2023, 10, 26));
}

TEST(ValidDateTest, InvalidYearTooLow)
{
    ASSERT_FALSE(ValidDate(1799, 10, 26));
}

TEST(ValidDateTest, InvalidYearTooHigh)
{
    ASSERT_FALSE(ValidDate(2201, 10, 26));
}

TEST(ValidDateTest, InvalidMonthTooLow)
{
    ASSERT_FALSE(ValidDate(2023, 0, 26));
}

TEST(ValidDateTest, InvalidMonthTooHigh)
{
    ASSERT_FALSE(ValidDate(2023, 13, 26));
}

TEST(ValidDateTest, InvalidDayTooLow)
{
    ASSERT_FALSE(ValidDate(2023, 10, 0));
}

TEST(ValidDateTest, InvalidDayTooHigh)
{
    ASSERT_FALSE(ValidDate(2023, 10, 32));
}

TEST(ValidDateTest, LeapYearValid)
{
    ASSERT_TRUE(ValidDate(2024, 2, 29));
}

TEST(ValidDateTest, LeapYearInvalid)
{
    ASSERT_FALSE(ValidDate(2023, 2, 29));
}

TEST(ValidDateTest, DaysInMonth)
{
    ASSERT_TRUE(ValidDate(2023, 2, 28));
    ASSERT_TRUE(ValidDate(2023, 4, 30));
    ASSERT_TRUE(ValidDate(2023, 1, 31));
}