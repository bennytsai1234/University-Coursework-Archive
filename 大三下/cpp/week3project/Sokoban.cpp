#include<iostream>
#include<curses.h>
#include<string>
#include<iomanip>
#include<sstream>
using namespace std;

void readMap(int n){
        //處理檔名
        char ch; // 讀取內容
        string filename;
        string tmp;
        int count[3] = {0}; //, B, D, W
        stringstream ss;
        ss << "map" << setw(3) << setfill('0') << n  << ".txt";
        ss >> filename;

        initscr();
        noecho();
        start_color();
        init_pair( 1, COLOR_CYAN, COLOR_BLACK );// H
        init_pair( 2, COLOR_RED, COLOR_BLACK );// B
        init_pair( 3, COLOR_WHITE, COLOR_GREEN );// D, C
        init_pair( 4, COLOR_MAGENTA, COLOR_BLACK );// W

        move(0, 0);
        FILE* fp = fopen(filename.c_str(),  "r");
        while(fscanf(fp, "%c", &ch) != EOF){
                switch(ch){
                        case 'H':
                                attron(COLOR_PAIR(1));
                                addch(ch);
                                attroff(COLOR_PAIR(1));
                                break;
                        case 'B':
                                attron(COLOR_PAIR(2));
                                addch(ch);
                                attroff(COLOR_PAIR(2));
                                count[0] += 1;
                                break;
                        case 'D': case 'C':
                                attron(COLOR_PAIR(3));
                                addch(ch);
                                attroff(COLOR_PAIR(3));
                                if(ch == 'D') count[1] += 1;
                                break;
                        case 'W':
                                attron(COLOR_PAIR(4));
                                addch(ch);
                                attroff(COLOR_PAIR(4));
                                count[2] += 1;
                                break;
                        case ' ': case '\n':
                                addch(ch);
                                break;
                        default:
                                printw("MAP IS INVALID!");
                                break;
                }
        }
        if(count[2] == 1 && count[0] == count[1]) refresh();
        else printw("MAP IS INVALID!");
        printw("PRESS ANY BUTTON");
        getch();
        endwin();
}

int main(){
        int n = 0;
        int ch;
        cin >> n;
        readMap(n);
}