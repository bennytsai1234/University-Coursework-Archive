#include "request.h"
#ifndef MYREQUEST_H
#define MYREQUEST_H
class MyRequest : public CRequest {
public:
    MyRequest(const string s = ""): CRequest(s) {}
    MyRequest& operator<<(const string s);
    MyRequest& operator>>(string& s);
};
#endif
