#include <iostream>
#include <string>
#include <curl/curl.h>

using namespace std;

int main() {
    CURL *curl;
    CURLcode res;

    curl = curl_easy_init();
    if(curl) {
        string postData = "STUID=110321006";
    
        curl_easy_setopt(curl, CURLOPT_URL, "http://lilina:8000/login");
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, postData.c_str());
        res = curl_easy_perform(curl);
        if(res != CURLE_OK) {
            cerr << "curl_easy_perform() failed: " << curl_easy_strerror(res) << endl;
        }
        curl_easy_cleanup(curl);
    } else {
        cerr << "Failed to initialize curl" << endl;
    }
    
    return 0;
}
