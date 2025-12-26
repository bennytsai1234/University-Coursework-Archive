#include <iostream>
#include <string>
#include "CRequest.h"

using std::cin;
using std::cout;
using std::endl;
using std::string;

#define GAME_SERVER_URL "http://lilina.csie.ncnu.edu.tw:5000/guess"

int main()
{
    CRequest request(GAME_SERVER_URL);
    string guess;
    request.post("LINE=/new");
    string game_id = request.read();
    cout << "Guess an integer between 1 and 100." << endl;
    while (true)
    {
        cout << "x=?";
        cin >> guess;
        request.post("LINE=" + game_id + " " + guess);
        string response = request.read();
        if (response == "Too large")
        {
            cout << "Too large" << endl;
        }
        else if (response == "Too small")
        {
            cout << "Too small" << endl;
        }
        else
        {
            cout << response << endl;
            break;
        }
    }

    return 0;
}
