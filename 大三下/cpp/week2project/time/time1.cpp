/* ctime example */
#include <iostream>
#include <ctime>
int main ()
{
time_t t;
time ( &t );
std::cout << "The current local time is: "
<< ctime (&t) << std::endl;
return 0;
}