#include <iostream>
#include <ctime>

int main() {
    time_t currentTime = time(nullptr);
    
    // 將當前時間轉換為當地時間
    struct tm *localTime = localtime(&currentTime);
    
    // 定義星期幾的字串陣列
    const char* weekdays[] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
    
    // 取得星期幾的索引
    int weekdayIndex = localTime->tm_wday;
    
    // 取得年、月、日
    int year = localTime->tm_year + 1900;
    int month = localTime->tm_mon + 1;
    int day = localTime->tm_mday;
    
    // 輸出結果
    std::cout << weekdays[weekdayIndex] << " " << year << "-" << month << "-" << day << std::endl;
    
    return 0;
}
