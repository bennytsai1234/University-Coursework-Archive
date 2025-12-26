#include <iostream>
using std::cout;
using std::endl;

struct Rational
{
    int numerator;
    int denominator;
};

void print_array(Rational a[], int n)
{
    for (int i = 0; i < n; ++i)
    {
        cout << a[i].numerator;
        if (a[i].denominator != 1)
            cout << '/' << a[i].denominator;
        if (i != n - 1)
            cout << ' ';
        else
            cout << '\n';
    }
}

int cmp(const void *p1, const void *p2);

int main()
{
    Rational A[] = {
        {1, 1}, {1, 2}, {2, 1}, {1, 3}, {3, 1}, {1, 4}, {4, 1}};
    /*   1/1,    1/2,    2/1,    1/3,    3/1,    1/4,    4/1     */
    print_array(A, sizeof(A) / sizeof(A[0]));
    qsort(A, sizeof(A) / sizeof(A[0]), sizeof(A[0]), cmp);
    print_array(A, sizeof(A) / sizeof(A[0]));

    Rational B[] = {
        {1, 1}, {1, 2}, {2, 2}, {2, 3}, {3, 3}, {3, 4}, {4, 4}, {4, 5}, {5, 5}
    };
    print_array(B, sizeof(B)/sizeof(B[0]));
    qsort(B, sizeof(B)/sizeof(B[0]), sizeof(B[0]), cmp);
    print_array(B, sizeof(B)/sizeof(B[0]));
    return 0;
}

int cmp(const void *p1, const void *p2)
{

    const Rational *r1 = static_cast<const Rational *>(p1);
    const Rational *r2 = static_cast<const Rational *>(p2);

    return r1->numerator * r2->denominator - r2->numerator * r1->denominator;
}