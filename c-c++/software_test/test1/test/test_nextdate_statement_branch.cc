#include "gtest/gtest.h"
#include "nextdate.h"

// 语句覆盖和分支覆盖测试用例

// 1. 一般情况，覆盖大部分语句和分支
TEST(NextDateTest, SimpleTest)
{
    int year = 2023, month = 10, day = 26;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2023);
    ASSERT_EQ(month, 10);
    ASSERT_EQ(day, 27);
    // 覆盖：ValidDate, month == 1 || 3 || 5 || 7 || 8 || 10, day != 31
    // 分支：ValidDate返回true, month == 1 || 3 || 5 || 7 || 8 || 10为true, day == 31为false
}

// 2. 月末情况，覆盖部分语句和分支
TEST(NextDateTest, EndOfMonthTest)
{
    int year = 2023, month = 10, day = 31;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2023);
    ASSERT_EQ(month, 11);
    ASSERT_EQ(day, 1);
    // 覆盖：ValidDate, month == 1 || 3 || 5 || 7 || 8 || 10, day == 31
    // 分支：ValidDate返回true, month == 1 || 3 || 5 || 7 || 8 || 10为true, day == 31为true
}

// 3. 年末情况，覆盖部分语句和分支
TEST(NextDateTest, EndOfYearTest)
{
    int year = 2023, month = 12, day = 31;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2024);
    ASSERT_EQ(month, 1);
    ASSERT_EQ(day, 1);
    // 覆盖：ValidDate, month == 12, day == 31
    // 分支：ValidDate返回true, month == 12为true, day == 31为true
}

// 4. 闰年2月29日，覆盖闰年分支
TEST(NextDateTest, LeapYearTest)
{
    int year = 2024, month = 2, day = 29;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2024);
    ASSERT_EQ(month, 3);
    ASSERT_EQ(day, 1);
    // 覆盖：ValidDate, month == 2, LeapYear, day == 29
    // 分支：ValidDate返回true, month == 2为true, LeapYear为true, day == 29为true
}

// 5. 非闰年2月28日，覆盖非闰年分支
TEST(NextDateTest, NonLeapYearTest)
{
    int year = 2023, month = 2, day = 28;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2023);
    ASSERT_EQ(month, 3);
    ASSERT_EQ(day, 1);
    // 覆盖：ValidDate, month == 2, !LeapYear, day == 28
    // 分支：ValidDate返回true, month == 2为true, LeapYear为false, day == 28为true
}

// 6. 无效日期，覆盖无效日期分支
TEST(NextDateTest, InvalidDateTest)
{
    int year = 2023, month = 2, day = 30;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2023);
    ASSERT_EQ(month, 2);
    ASSERT_EQ(day, 30);
    // 覆盖：ValidDate返回false
    // 分支：ValidDate返回false
}

TEST(ValidDateTest, ValidDate)
{
    ASSERT_TRUE(ValidDate(2023, 10, 26));
    // 覆盖：ValidDate所有判断都为true的情况
}

TEST(ValidDateTest, InvalidYearTooLow)
{
    ASSERT_FALSE(ValidDate(1799, 10, 26));
    // 覆盖：year < 1800
}

TEST(ValidDateTest, InvalidYearTooHigh)
{
    ASSERT_FALSE(ValidDate(2201, 10, 26));
    // 覆盖：year > 2200
}

TEST(ValidDateTest, InvalidMonthTooLow)
{
    ASSERT_FALSE(ValidDate(2023, 0, 26));
    // 覆盖：month < 1
}

TEST(ValidDateTest, InvalidMonthTooHigh)
{
    ASSERT_FALSE(ValidDate(2023, 13, 26));
    // 覆盖：month > 12
}

TEST(ValidDateTest, InvalidDayTooLow)
{
    ASSERT_FALSE(ValidDate(2023, 10, 0));
    // 覆盖：day < 1
}

TEST(ValidDateTest, InvalidDayTooHigh)
{
    ASSERT_FALSE(ValidDate(2023, 10, 32));
    // 覆盖：day > daysInMonth[month]
}

TEST(ValidDateTest, LeapYearValid)
{
    ASSERT_TRUE(ValidDate(2024, 2, 29));
    // 覆盖：LeapYear为true，且day有效
}

TEST(ValidDateTest, LeapYearInvalid)
{
    ASSERT_FALSE(ValidDate(2023, 2, 29));
    // 覆盖：LeapYear为false，且day无效
}

TEST(ValidDateTest, DaysInMonth)
{
    ASSERT_TRUE(ValidDate(2023, 2, 28));
    ASSERT_TRUE(ValidDate(2023, 4, 30));
    ASSERT_TRUE(ValidDate(2023, 1, 31));
    // 覆盖：daysInMonth数组的不同取值
}