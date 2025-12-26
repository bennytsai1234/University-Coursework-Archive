#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
#include <fstream>
#include <cctype>
using namespace std;
int main()
{
    string line;
    int value;
    int count = 0;
    int first;
    ofstream intfile("INTFILE");
    ofstream symfile("SYMTAB");
    while (getline(cin, line))
    {
        istringstream ass(line);
        istringstream bss(line);
        string word;
        bool hasAlpha = false;
        if (isalpha(line[0]))
        {
            hasAlpha = true;
        }
        if (hasAlpha)
        {
            ass >> word;
            symfile << setfill(' ') << left << setw(7) << word << right;
        }
        while (bss >> word)
        {

            if (word == "START")
            {
                bss >> word;
                istringstream(word) >> hex >> value;
                first = value;
                intfile << setfill('0') << setw(6) << uppercase << hex << value << dec;
                intfile << " " << line << endl;
                symfile << setfill('0') << setw(6) << uppercase << hex << value << dec << " ";
                symfile << setfill('0') << setw(6) << uppercase << hex << value << dec << endl;
            }
            else if (word == "RESW")
            {
                bss >> word;
                symfile << setfill('0') << setw(6) << uppercase << hex << value << dec << endl;
                intfile << setfill('0') << setw(6) << uppercase << hex << value << dec;
                intfile << " " << line << endl;
                int reg;
                istringstream(word) >> dec >> reg;
                reg *= 3;
                value += reg;
            }
            else if (word == "BYTE")
            {
                bss >> word;
                symfile << setfill('0') << setw(6) << uppercase << hex << value << dec << endl;
                intfile << setfill('0') << setw(6) << uppercase << hex << value << dec;
                intfile << " " << line << endl;
                if (word[0] == 'C')
                {
                    int length = word.length() - 3;
                    value += length;
                }
                else if (word[0] == 'X')
                {
                    int length = word.length() - 3;
                    value += length / 2;
                }
            }
            else if (word == "RESB")
            {
                bss >> word;
                symfile << setfill('0') << setw(6) << uppercase << hex << value << dec << endl;
                intfile << setfill('0') << setw(6) << uppercase << hex << value << dec;
                intfile << " " << line << endl;
                int reg;
                istringstream(word) >> dec >> reg;
                value += reg;
            }
            else if (word == "WORD")
            {
                bss >> word;
                symfile << setfill('0') << setw(6) << uppercase << hex << value << dec << endl;
                intfile << setfill('0') << setw(6) << uppercase << hex << value << dec;
                intfile << " " << line << endl;
                value += 3;
            }
            else if (word == "JGT" || word == "LDA" || word == "MUL" ||
                     word == "DIV" || word == "STA" || word == "JSUB" || word == "RSUB" ||
                     word == "LDX" || word == "TD" || word == "JEQ" ||
                     word == "RD" || word == "STCH" || word == "TIX" ||
                     word == "JLT" || word == "LDCH" || word == "END" ||
                     word == "LDL" || word == "ADD" || word == "COMP" || word == "WD" ||
                     word == "STL" || word == "J" || word == "STX" || word == "SUB")
            {
                intfile << setfill('0') << setw(6) << uppercase << hex << value << dec;
                intfile << " " << line << endl;
                value += 3;
                if (hasAlpha)
                {
                    symfile << setfill('0') << setw(6) << uppercase << hex << value << dec << endl;
                }
            }
            if (word == "END")
            {
                value -= 3;
            }
        }
    }
    symfile.seekp(14);
    symfile << setfill('0') << setw(6) << uppercase << hex << (value - first) << dec << endl;
    symfile.close();
    intfile.close();
    return 0;
}
