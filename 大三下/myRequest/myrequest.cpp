#include "pch.h"
#include "myrequest.h"

MyRequest& MyRequest::operator<<(const string s) {
    post(s);
    return *this;
}

MyRequest& MyRequest::operator>>(string& s) {
    if (m_prevAction == "POST") {
        m_prevAction = "GET";
        s = m_response;        // Return the buffered response from POST
    } else {
        get();
        s = m_response;
    }
    return *this;
}
