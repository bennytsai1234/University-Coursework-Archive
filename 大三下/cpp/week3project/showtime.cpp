#include <iostream>
#include <ncurses.h>
#include <ctime>
#include <unistd.h>
using namespace std;

int main()
{
    // 初始化 ncurses
    initscr();
    start_color();
    keypad(stdscr, TRUE);
    curs_set(0);
    timeout(0);
    noecho();

    // 設置初始位置和顏色
    int X = (COLS / 2) - 4;
    int Y = LINES / 2;
    int tmp_color = 0;
    init_pair(1, COLOR_MAGENTA, COLOR_BLACK);
    init_pair(2, COLOR_YELLOW, COLOR_BLACK);
    init_pair(3, COLOR_CYAN, COLOR_BLACK);
    init_pair(4, COLOR_BLUE, COLOR_BLACK);
    init_pair(5, COLOR_RED, COLOR_BLACK);
    init_pair(6, COLOR_GREEN, COLOR_BLACK);
    init_pair(7, COLOR_WHITE, COLOR_BLACK);

    // 主循環
    while (true)
    {
        // 獲取用戶輸入
        int user_input = getch();
        if (user_input != ERR)
        {
            // 根據輸入移動位置
            switch (user_input)
            {
            case KEY_UP:
                Y--;
                break;
            case KEY_DOWN:
                Y++;
                break;
            case KEY_LEFT:
                X--;
                break;
            case KEY_RIGHT:
                X++;
                break;
            }
        }
        if (X < 0)
        {
            X = 0;
        }
        if (Y < 0)
        {
            Y = 0;
        }
        // 獲取當前時間並格式化
        time_t current_time;
        time(&current_time);
        struct tm *time_info = localtime(&current_time);
        char time_buffer[9];
        strftime(time_buffer, sizeof(time_buffer), "%T", time_info);

        // 移動游標並根據輸入設置顏色
        move(Y, X);
        if (user_input <= '7' && user_input >= '0')
        {
            int color_index = user_input - '0';
            attroff(COLOR_PAIR(tmp_color));
            attron(COLOR_PAIR(color_index));
            tmp_color = color_index;
        }
        else
        {
            addstr(time_buffer);
        }

        // 刷新螢幕並延遲
        refresh();
        clear();
        usleep(30000);
    }

    // 關閉 ncurses
    endwin();
    return 0;
}
