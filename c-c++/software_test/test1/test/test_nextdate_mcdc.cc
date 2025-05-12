#include "gtest/gtest.h"
#include "nextdate.h"

// MCDC覆盖测试用例

// ValidDate 函数的条件：
// 1. year >= 1800
// 2. year <= 2200
// 3. month >= 1
// 4. month <= 12
// 5. day >= 1
// 6. day <= daysInMonth[month]

// 1. 测试用例：year >= 1800 独立影响判定结果
TEST(ValidDateTest, MCDC_YearLowerBound)
{
    // a. year = 1799, month = 10, day = 26  -> ValidDate(false)
    ASSERT_FALSE(ValidDate(1799, 10, 26));
    // b. year = 1800, month = 10, day = 26  -> ValidDate(true)
    ASSERT_TRUE(ValidDate(1800, 10, 26));
    // 结论：year >= 1800 独立影响判定结果
}

// 2. 测试用例：year <= 2200 独立影响判定结果
TEST(ValidDateTest, MCDC_YearUpperBound)
{
    // a. year = 2201, month = 10, day = 26  -> ValidDate(false)
    ASSERT_FALSE(ValidDate(2201, 10, 26));
    // b. year = 2200, month = 10, day = 26  -> ValidDate(true)
    ASSERT_TRUE(ValidDate(2200, 10, 26));
    // 结论：year <= 2200 独立影响判定结果
}

// 3. 测试用例：month >= 1 独立影响判定结果
TEST(ValidDateTest, MCDC_MonthLowerBound)
{
    // a. year = 2023, month = 0, day = 26  -> ValidDate(false)
    ASSERT_FALSE(ValidDate(2023, 0, 26));
    // b. year = 2023, month = 1, day = 26  -> ValidDate(true)
    ASSERT_TRUE(ValidDate(2023, 1, 26));
    // 结论：month >= 1 独立影响判定结果
}

// 4. 测试用例：month <= 12 独立影响判定结果
TEST(ValidDateTest, MCDC_MonthUpperBound)
{
    // a. year = 2023, month = 13, day = 26  -> ValidDate(false)
    ASSERT_FALSE(ValidDate(2023, 13, 26));
    // b. year = 2023, month = 12, day = 26  -> ValidDate(true)
    ASSERT_TRUE(ValidDate(2023, 12, 26));
    // 结论：month <= 12 独立影响判定结果
}

// 5. 测试用例：day >= 1 独立影响判定结果
TEST(ValidDateTest, MCDC_DayLowerBound)
{
    // a. year = 2023, month = 10, day = 0  -> ValidDate(false)
    ASSERT_FALSE(ValidDate(2023, 10, 0));
    // b. year = 2023, month = 10, day = 1  -> ValidDate(true)
    ASSERT_TRUE(ValidDate(2023, 10, 1));
    // 结论：day >= 1 独立影响判定结果
}

// 6. 测试用例：day <= daysInMonth[month] 独立影响判定结果
TEST(ValidDateTest, MCDC_DayUpperBound)
{
    // a. year = 2023, month = 10, day = 32  -> ValidDate(false)
    ASSERT_FALSE(ValidDate(2023, 10, 32));
    // b. year = 2023, month = 10, day = 31  -> ValidDate(true)
    ASSERT_TRUE(ValidDate(2023, 10, 31));
    // 结论：day <= daysInMonth[month] 独立影响判定结果
}