#include "rational.h"

int main()
{
   CRational a(1, 4);
   CRational b(3, 4);
   CRational c = a+b;
   c.Print();
   c.Reduction(); c.Print();
   CRational d = c; d.Print();
   CRational e(c); e.Print();
   return 0;
}