#include "gtest/gtest.h"
#include "nextdate.h"

// 判定覆盖和条件覆盖测试用例

// 1. 有效日期，非月末，非年末
TEST(NextDateTest, ValidDateNotEndOfMonthNotEndOfYear)
{
    int year = 2023, month = 10, day = 26;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2023);
    ASSERT_EQ(month, 10);
    ASSERT_EQ(day, 27);
    // 判定：ValidDate(true), month == 1 || 3 || 5 || 7 || 8 || 10 (false), month == 4 || 6 || 9 || 11 (false), month == 12 (false), LeapYear(不涉及), day == 31 (false), day == 30 (false), day == 29 (false), day == 28 (false)
    // 条件：year >= 1800 (true), year <= 2200 (true), month >= 1 (true), month <= 12 (true), day >= 1 (true), day <= daysInMonth[month] (true)
}

// 2. 有效日期，月末，非年末
TEST(NextDateTest, ValidDateEndOfMonthNotEndOfYear)
{
    int year = 2023, month = 4, day = 30;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2023);
    ASSERT_EQ(month, 5);
    ASSERT_EQ(day, 1);
    // 判定：ValidDate(true), month == 1 || 3 || 5 || 7 || 8 || 10 (false), month == 4 || 6 || 9 || 11 (true), month == 12 (false), LeapYear(不涉及), day == 30 (true)
    // 条件：year >= 1800 (true), year <= 2200 (true), month >= 1 (true), month <= 12 (true), day >= 1 (true), day <= daysInMonth[month] (true)
}

// 3. 有效日期，年末
TEST(NextDateTest, ValidDateEndOfYear)
{
    int year = 2023, month = 12, day = 31;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2024);
    ASSERT_EQ(month, 1);
    ASSERT_EQ(day, 1);
    // 判定：ValidDate(true), month == 1 || 3 || 5 || 7 || 8 || 10 (false), month == 4 || 6 || 9 || 11 (false), month == 12 (true), LeapYear(不涉及), day == 31 (true)
    // 条件：year >= 1800 (true), year <= 2200 (true), month >= 1 (true), month <= 12 (true), day >= 1 (true), day <= daysInMonth[month] (true)
}

// 4. 有效日期，闰年2月
TEST(NextDateTest, ValidDateLeapYearFebruary)
{
    int year = 2024, month = 2, day = 29;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2024);
    ASSERT_EQ(month, 3);
    ASSERT_EQ(day, 1);
    // 判定：ValidDate(true), month == 1 || 3 || 5 || 7 || 8 || 10 (false), month == 4 || 6 || 9 || 11 (false), month == 12 (false), LeapYear(true), day == 31 (false), day == 30 (false), day == 29 (true), day == 28 (false)
    // 条件：year >= 1800 (true), year <= 2200 (true), month >= 1 (true), month <= 12 (true), day >= 1 (true), day <= daysInMonth[month] (true)
}

// 5. 有效日期，非闰年2月
TEST(NextDateTest, ValidDateNonLeapYearFebruary)
{
    int year = 2023, month = 2, day = 28;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2023);
    ASSERT_EQ(month, 3);
    ASSERT_EQ(day, 1);
    // 判定：ValidDate(true), month == 1 || 3 || 5 || 7 || 8 || 10 (false), month == 4 || 6 || 9 || 11 (false), month == 12 (false), LeapYear(false), day == 31 (false), day == 30 (false), day == 29 (false), day == 28 (true)
    // 条件：year >= 1800 (true), year <= 2200 (true), month >= 1 (true), month <= 12 (true), day >= 1 (true), day <= daysInMonth[month] (true)
}

// 6. 无效日期
TEST(NextDateTest, InvalidDate)
{
    int year = 2023, month = 2, day = 30;
    NextDate(year, month, day);
    ASSERT_EQ(year, 2023);
    ASSERT_EQ(month, 2);
    ASSERT_EQ(day, 30);
    // 判定：ValidDate(false)
    // 条件：year >= 1800 (true), year <= 2200 (true), month >= 1 (true), month <= 12 (true), day >= 1 (true), day <= daysInMonth[month] (false)
}

// 7. 边界值测试：年份下界
TEST(NextDateTest, InvalidYearLowerBound)
{
    int year = 1799, month = 1, day = 1;
    ASSERT_FALSE(ValidDate(year, month, day));
    // 条件：year >= 1800 (false)
}

// 8. 边界值测试：年份上界
TEST(NextDateTest, InvalidYearUpperBound)
{
    int year = 2201, month = 1, day = 1;
    ASSERT_FALSE(ValidDate(year, month, day));
    // 条件：year <= 2200 (false)
}

// 9. 边界值测试：月份下界
TEST(NextDateTest, InvalidMonthLowerBound)
{
    int year = 2023, month = 0, day = 1;
    ASSERT_FALSE(ValidDate(year, month, day));
    // 条件：month >= 1 (false)
}

// 10. 边界值测试：月份上界
TEST(NextDateTest, InvalidMonthUpperBound)
{
    int year = 2023, month = 13, day = 1;
    ASSERT_FALSE(ValidDate(year, month, day));
    // 条件：month <= 12 (false)
}

// 11. 边界值测试：日期下界
TEST(NextDateTest, InvalidDayLowerBound)
{
    int year = 2023, month = 1, day = 0;
    ASSERT_FALSE(ValidDate(year, month, day));
    // 条件：day >= 1 (false)
}