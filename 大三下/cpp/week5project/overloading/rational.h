#include <iostream>
using std::cout;
using std::endl;
using std::istream;
using std::ostream;

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
#ifdef _DEBUG
        cout << "Constructor(" << p << "," << q << ") called" << endl;
#endif
    }

    CRational(const CRational &a)
    {
        p = a.p;
        q = a.q;
#ifdef _DEBUG
        cout << "Copy Constructor(" << p << "," << q << ") called" << endl;
#endif
    }

    CRational Addition(CRational input)
    {
        int tmp1 = p * input.q + input.p * q;
        int tmp2 = q * input.q;
        p = tmp1;
        q = tmp2;
        Reduction();
        return CRational(p, q);
    }
    CRational Mul(CRational input)
    {
        int tmp1 = p * input.p;
        int tmp2 = q * input.q;
        p = tmp1;
        q = tmp2;
        Reduction();
        return CRational(p, q);
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
            cout << p << "/" << q << endl;
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
    CRational operator*(const CRational &b)
    {
        return Mul(b);
    }
    friend istream &operator>>(istream &in, CRational &r);
    friend ostream &operator<<(ostream &in, const CRational &r);
};
istream &operator>>(istream &in, CRational &r)
{
    char slash;
    in >> r.p >> slash >> r.q;
    r.Reduction();
    return in;
}
ostream &operator<<(ostream &out, const CRational &r)
{
    out << r.p << "/" << r.q;
    return out;
}
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
