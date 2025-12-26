#include <iostream>
#include <fstream>
#include <sstream>
#include <unordered_map>
#include <iomanip>
using namespace std;

unordered_map<string, string> optab = {
    {"LDA", "00"},
    {"STA", "0C"},
    {"ADD", "18"},
    {"SUB", "1C"},
    {"MUL", "20"},
    {"DIV", "24"},
    {"JUMP", "3C"},
    {"JEQ", "30"},
    {"JLT", "38"},
    {"JSUB", "48"},
    {"RSUB", "4C"},
    {"COMP", "28"},
    {"CLEAR", "B4"},
    {"TIX", "2C"},
    {"TD", "E0"},
    {"RD", "D8"},
    {"WD", "DC"},
    {"RSUB", "4C"},
    {"LDCH", "50"},
    {"STCH", "54"},
    {"LDX", "04"},
    {"STX", "10"},
    {"LDB", "68"},
    {"STB", "78"},
    {"LDL", "08"},
    {"STL", "14"},
    {"JSUB", "48"},
    {"RSUB", "4C"},
};

int main() {
    string input;
    string t;
    string line;
    string loc, label, op, operand;
    string Trecord = "T";
    int start = 0;
    int countLen = 0;
    ifstream intfile("INTFILE");
    ifstream symtab("SYMTAB");

    unordered_map<string, string> hash;
    istringstream iss(line);
    string symbol, length, address;
    getline(symtab, line);
    iss >> symbol >> address >> length;
    hash[symbol] = address;
    while (getline(symtab, line)) {
        iss >> symbol >> hex >> address;
        hash[symbol] = address;
    }

    while (getline(intfile, input)) {
        istringstream iss(input);
        istringstream iss2(input);
        if (Trecord.size() >= 60) {
                stringstream ss;
                string tmp = Trecord.substr(10);
                int a = tmp.size();
                ss << hex << a;
                Trecord.replace(8, 2, ss.str());
                cout << Trecord << endl;
                iss2 >> t;
                Trecord = "T";
                Trecord = Trecord + t + "00";
        }


        while (iss >> t) {
            if (t == "START") {
                iss2 >> start >> line;
                cout << "H" << setw(6) << right << line << setfill('0') << setw(                                                                     6) << start << length << endl;
                iss >> t;
                Trecord = Trecord +"00"+ t + "00";
            }

            if (t != "END" && t != "START" && t != "BYTE" && t != "WORD") {
                auto it = optab.find(t);
                if (it != optab.end()) {
                    op = it->second;
                    Trecord += op;
                    iss >> t;
                    auto it = hash.find(t);
                    if (it != hash.end()) {
                        operand = it->second;
                        Trecord += operand.substr(2);
                    }
                    else {
                        Trecord += "0";
                    }
                }
            }
            else if ( t == "BYTE") {
                iss >> t;
                Trecord += t.substr(2, 2);
            }
            else if(t == "WORD"){
                iss >> t;
               
            }

            if (t == "END") {
                stringstream ss;
                string tmp = Trecord.substr(10);
                int a = tmp.size();
                ss << hex << a;
                Trecord.replace(8, 2, ss.str());
                cout << Trecord << endl;
                iss2 >> t;
                Trecord = "T";
                Trecord = Trecord + t + "00";
                cout << "E" << setfill('0') << setw(6)<< start << endl;
                break;
            }
        }

    }
}