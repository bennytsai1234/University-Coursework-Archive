#include <iostream>
#include <string>
using std::cout;
using std::endl;
using std::istream;
using std::ostream;
using std::stoi;
using std::string;

int gcd(int a, int b);

class CRational
{
public:
    int p = 0;
    int q = 1;

    CRational()
    {
#ifdef _DEBUG
        cout << "Constructor(" << p << "," << q << ") called" << endl;
#endif
    }

    CRational(int a, int b)
    {
        p = a;
        q = b;
        Reduction();
#ifdef _DEBUG
        cout << "Constructor(" << p << "," << q << ") called" << endl;
#endif
    }
    CRational(string a)
    {
        int position = a.find("/");
        if (position != std::string::npos)
        {
            p = stoi(a.substr(0, position));
            q = stoi(a.substr(position + 1));
        }
        else
        {
            p = stoi(a);
            q = 1;
        }
        Reduction();
#ifdef _DEBUG
        std::cout << "Constructor from string(" << p << "," << q << ") called" << std::endl;
#endif
    }
    CRational(const CRational &a)
    {
        p = a.p;
        q = a.q;
        Reduction();
#ifdef _DEBUG
        cout << "Copy Constructor(" << p << "," << q << ") called" << endl;
#endif
    }

    CRational Addition(CRational input)
    {
        int tmp1 = p * input.q + input.p * q;
        int tmp2 = q * input.q;
        return CRational(tmp1, tmp2);
    }
    CRational Subtract(CRational input)
    {
        int tmp1 = p * input.q - input.p * q;
        int tmp2 = q * input.q;
        return CRational(tmp1, tmp2);
    }
    CRational Mul(CRational input)
    {
        int tmp1 = p * input.p;
        int tmp2 = q * input.q;
        return CRational(tmp1, tmp2);
    }

    void Reduction()
    {
        int a = gcd(p, q);
        p /= a;
        q /= a;
    }

    void Print()
    {
        if (q != 0)
        {
            if (q == 1)
            {
                cout << p << endl;
            }
            else
            {
                cout << p << "/" << q << endl;
            }
        }

        else
        {
            cout << "分母為零" << endl;
        }
    }
    CRational operator+(const CRational &b)
    {
        return Addition(b);
    }
    CRational operator-(const CRational &b)
    {
        return Subtract(b);
    }
    CRational operator*(const CRational &b)
    {
        return Mul(b);
    }
    friend istream &operator>>(istream &in, CRational &r);
    friend ostream &operator<<(ostream &out, const CRational &r);
};

int gcd(int a, int b)
{
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
